from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField
from django.core.exceptions import ValidationError
from django.conf import settings
from apollo import forms, signals
from apollo.settings import apollo_settings
from apollo.lib import emails, recaptcha
from apollo.exceptions import RecaptchaVerificationException
import pdb
import requests
import copy
import json
import logging

logger = logging.getLogger(__name__)


#####-----< Layout >----#####
class Layout(models.Model):
    """ a layout controls the positioning and relative sizing of fields in a form."""
    name = models.CharField(max_length=150, unique=True)
    max_width = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self):
        return """%s (%s)""" % (
            self.name, self.id
        )


class LayoutField(models.Model):
    """ the positioning of a field in the forms' layout """
    layout = models.ForeignKey(Layout, related_name='blocks', on_delete=models.CASCADE)

    # width and height are in pct relative
    desktop_width = models.DecimalField(max_digits=6, decimal_places=3)
    desktop_height = models.DecimalField(max_digits=6, decimal_places=3)
    desktop_top_left = ArrayField(models.DecimalField(max_digits=6, decimal_places=3), size=2)

    mobile_width = models.DecimalField(max_digits=6, decimal_places=3)
    mobile_height = models.DecimalField(max_digits=6, decimal_places=3)
    mobile_top_left = ArrayField(models.DecimalField(max_digits=6, decimal_places=3), size=2)

    def __str__(self):
        return """%s x %s @ %s (%s)""" % (
            self.desktop_width, self.desktop_height, self.desktop_top_left, self.id
        )


#####-----< Forms >----#####
class Form(models.Model):
    layout = models.ForeignKey(Layout, related_name='forms', null=True, blank=True, default=None, on_delete=models.CASCADE)

    name = models.CharField(max_length=200, unique=True)

    redirect_url = models.CharField(max_length=150, null=True, blank=True, default=None)
    success_message = models.TextField(null=True, blank=True, default=None)
    submit_button_text = models.CharField(max_length=100, default='Submit')
    # if set, submissions go here instead of to our form submission endpoint
    submission_url = models.CharField(max_length=200, null=True, blank=True, default=None)
    # if set, these email addresses will be notified on submissions
    submission_contacts = ArrayField(models.CharField(max_length=400), null=True, blank=True, default=None)
    # if true, then we allow external hooks to listen for events occuring on this form (submissions, validation, etc.)
    allow_webhooks = models.BooleanField(default=False)
    # if true, forms will use recaptcha v3 for verification
    include_recaptcha = models.BooleanField(default=False)

    @classmethod
    def create_from_json(cls, form_data):
        """ instantiates a form instance and its associated fields from its serialized variation.

        :param: json_form `dict` parsed input form data (including field information)
        :return: `Form` the instantiated form instance
        :raises: `ValidationError` if the serializer is given invalid data
        """
        from apollo.api import serializers

        existing_form_field_template_names = set(FormFieldTemplate.objects.values_list('name', flat=True))

        form_serializer = serializers.FormSerializer(data=form_data)
        logger.debug('form data is {}'.format(form_data))
        if form_serializer.is_valid():
            # we need to create field templates for all fields don't currently exist for the form
            for form_field in form_serializer.validated_data['fields']:
                if form_field['name'] not in existing_form_field_template_names:
                    field_serializer = serializers.FormFieldTemplateSerializer(data=form_field)
                    if field_serializer.is_valid():
                        field_serializer.save()

            # then save the form and all fields to the DB
            return form_serializer.save()
        else:
            raise ValidationError('form serializer failed to deserialize with error(s) {}'.format(form_serializer.errors))

    def clone(self):
        """ clone this form to a new form. In addition to the basic fields of this model, this has the effect of copying:
        - associated form fields, creating new copies of fields for the new form

        :return: `Form` a clone of this form
        """
        form_copy = copy.deepcopy(self)

        # make a copy of the base form
        form_copy.pk = None
        form_copy.name = self.name + ' Copy'
        form_copy.save()

        # copy the fields
        for field in self.fields.all():
            field.pk = None
            field.form = form_copy
            field.save()

        return form_copy

    def process_submission(self, cleaned_data, request=None, submission=None):
        """ processes a form submission to clean the data in the form, trigger appropriate signal handlers, and run
        any post-creation validation steps. If `submission` is provided, it means we are processing an existing submission,
        as opposed to creating a new one """
        signals.form_submitted.send(
            sender=self.__class__,
            form_id=self.id,
            raw_data=cleaned_data,
            request=request
        )

        is_existing_submission = submission is not None
        if is_existing_submission:
            submission.raw_data = cleaned_data['raw_data']
        else:
            submission = FormSubmission(raw_data=cleaned_data['raw_data'], form=self)
            submission.created_by = request.user if hasattr(request, 'user') and request.user and not request.user.is_anonymous else None

        error_msg = False

        try:
            submission.clean_data(is_update=is_existing_submission)
        except ValueError as exc:
            error_msg = 'got error cleaning submission data'
        except ValidationError as exc:
            error_msg = 'got error validating submission data'
        finally:
            submission.save()

        # if the submission should be recaptcha protected, verify the recaptcha
        if self.include_recaptcha:
            logger.debug('form %s requests recaptcha checks, checking token now' % self.id)

            try:
                recaptcha_valid = recaptcha.verify_token(cleaned_data.get('recaptcha_token'), recaptcha_secret_key=apollo_settings.RECAPTCHA_SECRET_KEY)
                if not recaptcha_valid:
                    error_msg = 'recaptcha token is invalid'
            except RecaptchaVerificationException:
                error_msg = 'recaptcha verification failed with an error'

        if error_msg:
            signals.form_submission_error.send(
                sender=self.__class__,
                form_id=submission.form_id,
                raw_data=submission.raw_data,
                error=error_msg,
                request=request
            )

            raise ValidationError(error_msg)

        if self.submission_contacts and apollo_settings.SUBMISSION_EMAIL_FROM:
            emails.send(
                from_email=apollo_settings.SUBMISSION_EMAIL_FROM,
                to_emails=self.submission_contacts,
                subject='Apollo: New Form Submission',
                content='new form submission, data = %s' % str(submission.cleaned_data)
            )

        signals.form_submission_cleaned.send(
            sender=self.__class__,
            form_id=submission.form_id,
            submission_id=submission.id,
            cleaned_data=submission.cleaned_data,
            request=request,
            is_update=is_existing_submission
        )

        if is_existing_submission:
            signals.form_submission_updated.send(
                sender=self.__class__,
                form_id=submission.form_id,
                submission_id=submission.id,
                cleaned_data=submission.cleaned_data,
                request=request
            )

        return submission

    def __str__(self):
        return """%s (%s)""" % (self.name, self.id)

    class Meta:
        ordering = ['name']


class FormFieldTemplate(models.Model):
    FIELD_TYPES = [
        ('TEXT', 'TEXT'),
        ('HIDDEN', 'HIDDEN'),
        ('TEXTAREA', 'TEXTAREA'),
        ('SELECT', 'SELECT'),
        ('CHECKBOX', 'CHECKBOX'),
        ('RICHTEXT', 'RICHTEXT'),
        ('RADIO', 'RADIO'),
    ]

    RULE_OPTIONAL = 'OPTIONAL'
    RULE_REQUIRED = 'REQUIRED'
    RULE_EMAIL = 'EMAIL'
    RULE_PHONE_NUMBER = 'PHONE_NUMBER'
    VALIDATION_RULES = [(x, x) for x in [RULE_OPTIONAL, RULE_REQUIRED, RULE_EMAIL, RULE_PHONE_NUMBER]]

    LABEL_TOP = 'TOP'
    LABEL_RIGHT = 'RIGHT'
    LABEL_BOTTOM = 'BOTTOM'
    LABEL_LEFT = 'LEFT'
    LABEL_POSITIONS = [
        (LABEL_TOP, LABEL_TOP),
        (LABEL_RIGHT, LABEL_RIGHT),
        (LABEL_BOTTOM, LABEL_BOTTOM),
        (LABEL_LEFT, LABEL_LEFT),
    ]

    # If True, it means that the value of this field in a submission should be used as the primary label for
    # for the submission
    is_submission_label = models.BooleanField(default=False)

    # Core Fields (Not Overriddeable on FormField instances)
    name = models.CharField(max_length=100, unique=True)
    input_type = models.CharField(max_length=50, choices=FIELD_TYPES, default='text')
    is_visible = models.BooleanField(default=True)

    label = models.CharField(max_length=511, null=True, blank=True, default=None)
    label_position = models.CharField(max_length=50, choices=LABEL_POSITIONS, default=LABEL_TOP)
    placeholder = models.CharField(max_length=150, null=True, blank=True, default=None)
    default_value = models.CharField(max_length=500, null=True, blank=True, default=None)

    value_choices = ArrayField(
        ArrayField(models.CharField(max_length=100), size=2),
        null=True,
        blank=True,
        default=None
    )
    validation_rule = models.CharField(max_length=50, null=True, blank=True, default=RULE_REQUIRED, choices=VALIDATION_RULES)
    validation_message = models.CharField(max_length=255, null=True, blank=True, default=None)

    def __str__(self):
        return """%s // %s (%s)""" % (self.name, self.input_type, self.id)


class FormField(models.Model):
    """ a form field is a concrete instance of a field on a form. It must be separate from a FormFieldTemplate
    because while the template governs the common configuration of a field, there are certain properties which
    might need overriding on a per-form basis (designated by a leyou ading _)
    """
    form = models.ForeignKey(Form, related_name='fields', on_delete=models.CASCADE)
    template = models.ForeignKey(FormFieldTemplate, related_name='instances', on_delete=models.CASCADE)
    layout = models.ForeignKey(LayoutField, null=True, blank=True, default=None, on_delete=models.SET_NULL)

    label = models.CharField(max_length=511, null=True, blank=True, default=None)
    label_position = models.CharField(max_length=50, null=True, blank=True, default=FormFieldTemplate.LABEL_TOP, choices=FormFieldTemplate.LABEL_POSITIONS)
    default_value = models.CharField(max_length=500, null=True, blank=True, default=None)
    placeholder = models.CharField(max_length=150, null=True, blank=True, default=None)

    index = models.IntegerField(default=0)

    value_choices = ArrayField(
        ArrayField(models.CharField(max_length=100), size=2),
        null=True,
        blank=True,
        default=None
    )
    validation_rule = models.CharField(max_length=50, null=True, blank=True, default=FormFieldTemplate.RULE_REQUIRED, choices=FormFieldTemplate.VALIDATION_RULES)
    validation_message = models.CharField(max_length=255, null=True, blank=True, default=None)

    @property
    def name(self):
        return self.template.name

    @property
    def input_type(self):
        return self.template.input_type

    @property
    def is_visible(self):
        return self.template.is_visible and self.template.input_type != 'HIDDEN'

    @property
    def is_submission_label(self):
        return self.template.is_submission_label

    @property
    def is_required(self):
        return self.validation_rule != FormFieldTemplate.RULE_OPTIONAL

    def __str__(self):
        return """%s // Form %s (%s)""" % (
            self.name, self.form, self.id
        )


#####-----< Submissions >----#####
class FormSubmission(models.Model):
    form = models.ForeignKey(Form, related_name='submissions', on_delete=models.CASCADE)

    raw_data = JSONField()
    cleaned_data = JSONField(blank=True, null=True, default=None)

    is_valid = models.BooleanField(default=True)

    created_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, default=None, on_delete=models.SET_NULL)

    @property
    def label(self):
        """ the label for this submission is governed by the templates of the fields of the form. The first template
        which has `is_submission_label = True` has its field value looked up in the cleaned data and used as the submissions'
        label
        """
        labelling_field = self.form.fields.filter(template__is_submission_label=True).first()

        if not labelling_field or not self.cleaned_data:
            return None

        return self.cleaned_data[labelling_field.name]

    def clean_data(self, is_update=False):
        """ raw_data => cleaned_data. Cleaning is the process of:
        - removing fields from the raw data any fields which don't exist on the form being submitted
        - converting the raw_data, which will be a list of field dictionaries containing data submitted by the client,
        into a dictionary of field name -> field value
        - validating the data
        :param: `is_update` if true, we are updating an existing submission
        :return: `dict` of cleaned, validated data
        :raises: ValidationError if the submission fails to validate
        :raises: ValueError if data isn't available to clean / validate
        """
        # raw_data can be of form {'fields': [<field data>]} or [<field data]
        try:
            fields_list = self.raw_data['fields']
        except TypeError:
            fields_list = self.raw_data

        if not fields_list:
            raise ValueError('no data was found in the raw_data')

        named_data = {}

        existing_field_data = self.cleaned_data if is_update and self.cleaned_data is not None else {}
        # transform the fields list into a dictionary, indexed by field names
        fields_dict = {f['name']: f for f in fields_list}

        stored_defaults = dict(self.form.fields.all().values_list('template__name', 'default_value'))

        for fname in stored_defaults:
            if stored_defaults[fname] or fname in fields_dict or fname in existing_field_data:
                try:
                    named_data[fname] = fields_dict[fname]['value']
                except KeyError:
                    try:
                        named_data[fname] = existing_field_data[fname]
                    except KeyError:
                        named_data[fname] = stored_defaults[fname]

        sform = forms.SubmissionForm(apollo_fields=self.form.fields.all(), data=named_data)

        self.is_valid = sform.is_valid()

        if self.is_valid:
            self.cleaned_data = sform.cleaned_data
        else:
            raise ValidationError(json.dumps(sform.errors.as_json()))

        return self.cleaned_data

    def __str__(self):
        return """Submission for %s @ %s (%s)""" % (
            self.form, self.created_time, self.id
        )

    class Meta:
        ordering = ['-created_time', 'is_valid']
        permissions = (
            ("can_view_submissions", "Can View Form Submissions"),
            ("can_download_submissions", "Can Download Form Submissions"),
        )


#####-----< API >----#####
class APIUser(models.Model):
    """ an APIUser is the only type we allow to authenticate with Token auth (as opposed to session auth) """
    auth_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='apis', on_delete=models.CASCADE)
    service_name = models.CharField(max_length=200)

    def __str__(self):
        return """%s -- API = %s (%s)""" % (
            self.auth_user, self.service_name, self.id
        )


class ExternalWebhook(models.Model):
    """ an external webhook is a URL to which we POST when an event occurs against a Form (or child object) """
    # the allowed events define the possible events a webhook might be registered to listen on (one per hook)
    EVENT_SUBMISSION_CREATED = "new form submission"
    ALLOWED_EVENTS = (
        (EVENT_SUBMISSION_CREATED, EVENT_SUBMISSION_CREATED),
    )

    form = models.ForeignKey(Form, related_name='external_hooks', on_delete=models.CASCADE)

    url = models.CharField(max_length=255)
    for_event = models.CharField(max_length=100, choices=ALLOWED_EVENTS)
    # the name of the service registering a hook
    service = models.CharField(max_length=100)

    def send_data(self, data):
        """ send the given data to this webhooks' URL """
        err = resp = None

        try:
            resp = requests.post(self.url, json=data)
        except Exception as exc:
            # only request exceptions can occur here, so we blanket except
            err = str(exc)

        if resp is not None and not resp.ok:
            try:
                resp.raise_for_status()
            except requests.HTTPError as exc:
                err = str(exc)

        if err:
            signals.external_webhook_error.send(
                self.__class__,
                error=err,
                url=self.url,
                data=data
            )

        return resp.status_code if resp else None

    def __str__(self):
        return """%s: Send %s -> %s (%s)""" % (
            self.form.name, self.for_event, self.service.upper(), self.id
        )
