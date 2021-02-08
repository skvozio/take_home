from job_application.models import JobApplication
from rest_framework_gis import serializers
from rest_framework.serializers import URLField


class JobApplicationSerializer(serializers.GeoModelSerializer):
    url = URLField()



    class Meta:
        model = JobApplication
        fields = ('id', 'title', 'company_name', 'url', 'was_referred',
                  'contact_name', 'salary', 'address', 'date_applied', 'geo')
        read_only_fields = ['id', 'date_applied']
