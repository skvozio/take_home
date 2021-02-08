from django.urls import include, path
from rest_framework import routers
import job_application.views as views
from django.conf.urls import url
from job_application.views import schema_view


router = routers.DefaultRouter()
router.register(r'applications', views.JobApplicationViewSet, "applications")

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]