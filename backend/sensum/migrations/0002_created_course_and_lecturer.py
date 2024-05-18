# Generated by Django 5.0.4 on 2024-05-18 14:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('sensum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Updated')),
                ('name', models.CharField(max_length=60, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Updated')),
                ('title', models.CharField(max_length=120, unique=True)),
                ('primary_subtitle', models.CharField(blank=True, max_length=500, null=True)),
                ('secondary_subtitle', models.CharField(blank=True, max_length=500, null=True)),
                ('duration', models.DurationField(blank=True, null=True)),
                ('about_description', models.TextField()),
                ('audience_groups', models.ManyToManyField(to='auth.group', verbose_name='Audience Groups')),
                ('sponsors', models.ManyToManyField(to='sensum.sponsor')),
                ('lecturers', models.ManyToManyField(to='sensum.lecturer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
