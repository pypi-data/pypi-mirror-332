from django.core.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, permissions, status, views, authentication
from rest_framework.decorators import action
from rest_framework.response import Response
from pydoc import locate
from apollo.models import Form, FormFieldTemplate, FormField, FormSubmission, Layout
from apollo.settings import apollo_settings
from .serializers import *
from .permissions import FormSubmissionsPermission
import pdb


class FormViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows forms to be viewed, created, updated, or deleted.

    retrieve:
    Returns a Form instance.

    Permissions Required: `null`

    list:
    Returns all Forms.

    Permissions Required: `null`

    create:
    Creates a new Form instance. The forms' Layout and Fields to include in the form are also pass-able here.

    Permissions Required: `apollo_add_form`

    update:
    Updates a Form instance.

    Permissions Required: `apollo_change_form`

    delete:
    Deletes a Form instance. Note: this will also remove all associated fields and submissions.

    Permissions Required: `apollo_remove_form`
    """
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name',)

    @action(detail=True, methods=['post'])
    def clone(self, request, pk=None):
        form = self.get_object()
        clone = form.clone()

        return Response(FormSerializer(clone).data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], url_path='import')
    def import_form(self, request, pk=None):
        imported = Form.create_from_json(request.data)
        return Response(FormSerializer(imported).data, status=status.HTTP_201_CREATED)


class FormFieldTemplateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FormFieldTemplates to be viewed, created, updated, or deleted.

    retrieve:
    Returns a FormFieldTemplate instance

    Permissions Required: `null`

    list:
    Returns all FormFieldTemplate instances

    Permissions Required: `null`

    create:
    Creates a new FormFieldTemplate instance.

    Permissions Required: `apollo_add_formfieldtemplate`

    update:
    Updates a FormFieldTemplate instance.

    Permissions Required: `apollo_change_formfieldtemplate`

    delete:
    Deletes a FormFieldTemplate instance.

    Permissions Required: `apollo_remove_formfieldtemplate`
    """
    queryset = FormFieldTemplate.objects.all()
    serializer_class = FormFieldTemplateSerializer
    permission_classes = (permissions.DjangoModelPermissions,)


class FormFieldViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows FormField instances to be viewed, created, updated, or deleted.

    retrieve:
    Returns a FormField instance

    Permissions Required: `null`

    list:
    Returns all FormField instances

    Permissions Required: `null`

    create:
    Creates a new FormField instance.

    Permissions Required: `apollo_add_formfield`

    update:
    Updates a FormField instance.

    Permissions Required: `apollo_change_formfield`

    delete:
    Deletes a FormField instance.

    Permissions Required: `apollo_delete_formfield`
    """
    queryset = FormField.objects.all()
    serializer_class = FormFieldSerializer
    permission_classes = (permissions.DjangoModelPermissions,)


class FormSubmissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Submission instances to be viewed, created, updated, or deleted.

    retrieve:
    Returns a FormSubmission instance

    Permissions Required: `is_staff = True`

    list:
    Returns all FormSubmission instances

    Permissions Required: `is_staff = True`

    create:
    Creates a new FormSubmission instance.

    Permissions Required: `null`

    update:
    Updates a FormSubmission instance.

    Permissions Required: `is_staff = True`

    delete:
    Deletes a FormSubmission instance.

    Permissions Required: `is_staff = True`
    """
    queryset = FormSubmission.objects.all()
    authentication_classes = (authentication.SessionAuthentication, authentication.BasicAuthentication, authentication.TokenAuthentication,)
    permission_classes = (FormSubmissionsPermission,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('form_id',)

    def create(self, request, *args, **kwargs):
        try:
            return super(FormSubmissionViewSet, self).create(request, *args, **kwargs)
        except ValidationError as exc:
            return Response({'error': exc.message}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super(FormSubmissionViewSet, self).update(request, *args, **kwargs)

    def get_serializer_class(self):
        logger.debug(f'using submission serializer at {apollo_settings.DEFAULT_FORM_SUBMISSION_SERIALIZER}')
        return locate(apollo_settings.DEFAULT_FORM_SUBMISSION_SERIALIZER)


class LayoutViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Layout instances to be viewed, created, updated, or deleted.

    retrieve:
    Returns a Layout instance

    Permissions Required: `null`

    list:
    Returns all Layout instances

    Permissions Required: `null`

    create:
    Creates a new Layout instance.

    Permissions Required: `apollo_add_layout`

    update:
    Updates a Layout instance.

    Permissions Required: `apollo_change_layout`

    delete:
    Deletes a Layout instance.

    Permissions Required: `apollo_delete_layout`
    """
    queryset = Layout.objects.all()
    serializer_class = LayoutSerializer
    permission_classes = (permissions.DjangoModelPermissions,)


class ExternalWebhookViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    """
    API endpoint that allows ExternalWebhook instances to be created and deleted.

    create:
    Creates a new ExternalWebhook instance.

    Permissions Required: `apollo_add_externalwebhook`

    delete:
    Deletes a ExternalWebhook instance

    Permissions Required: `apollo_delete_externalwebhook`
    """
    queryset = ExternalWebhook.objects.all()
    serializer_class = ExternalWebhookSerializer
    permission_classes = (permissions.DjangoModelPermissions,)
    authentication_classes = (authentication.SessionAuthentication, authentication.BasicAuthentication, authentication.TokenAuthentication,)


class FormFieldOptionsAPIView(views.APIView):
    """
    API endpoint that allows FormFieldOptions to be viewed.

    list:
    Returns all FormFieldOptions, including Widget Types (e.g. 'TEXT', 'SELECT'), Validation Rules (e.g. 'REQUIRED', 'OPTIONAL'),
    and Label Positions (e.g. 'TOP', 'LEFT')

    Permissions Required: `null`
    """
    def get(self, request, *args, **kwargs):
        serializer = FieldOptionsSerializer({
            'widget_types': [_[0] for _ in FormFieldTemplate.FIELD_TYPES],
            'validation_rules': [_[0] for _ in FormFieldTemplate.VALIDATION_RULES],
            'label_positions': [_[0] for _ in FormFieldTemplate.LABEL_POSITIONS]
        })

        return Response(serializer.data)
