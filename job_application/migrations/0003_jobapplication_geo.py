# Generated by Django 3.1.6 on 2021-02-08 00:57

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0002_jobapplication_date_applied'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='geo',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326, verbose_name='Location'),
        ),
    ]
