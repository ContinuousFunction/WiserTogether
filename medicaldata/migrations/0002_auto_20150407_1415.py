# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicaldata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicaldata',
            name='author',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='author_email',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='ckan_url',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='extras',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='groups',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='isopen',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='license',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='license_id',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='license_title',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='maintainer',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='maintainer_email',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='metadata_created',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='metadata_modified',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='name',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='notes',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='notes_rendered',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='num_resources',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='num_tags',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='organization',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='owner_org',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='private',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='ratings_average',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='ratings_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='relationships',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='resources',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='revision_id',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='state',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='tags',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='title',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='tracking_summary',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='type',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='url',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='version',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='medicaldata',
            name='id',
            field=models.CharField(max_length=1000, serialize=False, primary_key=True),
        ),
    ]
