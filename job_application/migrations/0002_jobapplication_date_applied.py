# Generated by Django 3.1.6 on 2021-02-07 18:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='date_applied',
            field=models.DateField(default=datetime.date.today),
        ),
    ]