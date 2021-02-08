# Generated by Django 3.1.6 on 2021-02-07 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('company_name', models.TextField(blank=True, max_length=255, null=True, verbose_name='Company Name')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('was_referred', models.BooleanField(blank=True, default=False)),
                ('contact_name', models.CharField(max_length=255, verbose_name='Contact name')),
                ('salary', models.IntegerField(verbose_name='Salary')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
            ],
        ),
    ]