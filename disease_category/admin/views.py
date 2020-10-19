# Django imports
from django.utils import timezone
from datetime import datetime, timedelta
from pyfcm import FCMNotification
from django.conf import settings

# Django REST framework imports
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import (
    APIView,
)
from rest_framework.exceptions import (
    ValidationError,
    AuthenticationFailed
)
from rest_framework.pagination import PageNumberPagination

# Application imports
from templates.error_template import (
    ErrorTemplate,
)
from api.permissions import (
    IsAdmin,
)

# Model imports
from disease_category.models import (
    DiseaseCategory
)

# Serialier imports
from disease_category.admin.serializers import (
    DiseaseCategorySerializer,
)


# List Role
class DiseaseCategoryView(generics.ListCreateAPIView):
    model = DiseaseCategory
    serializer_class = DiseaseCategorySerializer
    permission_classes = (IsAdmin,)
    pagination_class = None
    search_fields = (
        'name',
    )
    def get_queryset(self):
        return self.model.objects.filter(is_deleted=False).order_by('name')

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class DiseaseCategoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    model = DiseaseCategory
    serializer_class = DiseaseCategorySerializer
    permission_classes = (IsAdmin,)
    lookup_url_kwarg = 'disease_category_id'

    def get(self, request, *args, **kwargs):
        disease_category_id = self.kwargs.get(self.lookup_url_kwarg)
        disease_category = self.get_object(disease_category_id)

        # Get serializer
        serializer = self.serializer_class(instance=disease_category)

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        disease_category_id = self.kwargs.get(self.lookup_url_kwarg)
        disease_category = self.get_object(disease_category_id)

        # Get serializer
        serializer = self.serializer_class(disease_category, data=request.data)
        serializer.is_valid(raise_exception=False)
        data = request.data

        disease_category.__dict__.update(
            name=data.get('name'),
        )

        # Save to database
        disease_category.save()

        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        drug_category_id = self.kwargs.get(self.lookup_url_kwarg)
        drug_category = self.get_object(drug_category_id)

        drug_category.__dict__.update(
            is_deleted=True,
        )

        # Save to database
        drug_category.save()

        return Response({
            'message': 'Deleted successfully'
        })

    def get_object(self, object_id):
        obj = self.model.objects.filter(
            id=object_id,
            is_deleted=False
        ).first()

        if not obj:
            raise ValidationError(ErrorTemplate.DISEASE_CATEGORY_NOT_EXIST)

        return obj