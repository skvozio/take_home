from django.contrib.gis.db import models
from datetime import date


class JobApplication(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title', null=False, blank=False)
    company_name = models.TextField(max_length=255, null=True, blank=True, verbose_name='Company Name')
    url = models.URLField(null=True, blank=True, verbose_name="URL")
    was_referred = models.BooleanField(default=False, blank=True)
    contact_name = models.CharField(max_length=255, verbose_name="Contact name")
    salary = models.IntegerField(verbose_name="Salary")
    address = models.CharField(max_length=255, verbose_name="Address")
    date_applied = models.DateField(default=date.today)
    geo = models.PointField(verbose_name="Location", null=True)

    def __str__(self):
        return self.title
