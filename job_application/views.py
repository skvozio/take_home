from rest_framework import viewsets
from job_application.models import JobApplication
from job_application.serializers import JobApplicationSerializer
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from filters.mixins import (
    FiltersMixin,
)
from job_application.validations import applications_query_schema


class JobApplicationViewSet(FiltersMixin, viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    http_method_names = ['get', 'post']

    filter_mappings = {
        'id': 'id',
        'title': 'title__icontains',
        'address': 'address__icontains',
        'salary': 'salary',
        'contact_name': 'contact_name__icontains',
        'was_referred': 'was_referred',
        'date_applied': 'date_applied',
        'start': 'date_applied__gte',
        'end': 'date_applied__lte',
    }

    filter_validation_schema = applications_query_schema


"""
Swagger schema view
"""
schema_view = get_schema_view(
   openapi.Info(
      title="Job Applications API",
      default_version='v1',
      description="API to keep track of job applications",
      contact=openapi.Contact(email="maksim.buturlakin@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)