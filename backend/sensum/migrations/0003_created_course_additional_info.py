# Generated by Django 5.0.4 on 2024-05-18 15:01

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensum', '0002_created_course_and_lecturer'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseAdditionalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Updated')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='course',
            name='primary_subtitle',
            field=models.CharField(blank=True, default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='secondary_subtitle',
            field=models.CharField(blank=True, default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='additional_info',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='sensum.courseadditionalinfo'),
        ),
    ]
