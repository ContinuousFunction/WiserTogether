# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicaldata', '0002_auto_20150407_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='medicaldata',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='medicaldata',
            name='question_text',
        ),
        migrations.AlterField(
            model_name='medicaldata',
            name='num_resources',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='medicaldata',
            name='num_tags',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='medicaldata',
            name='ratings_count',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='medicalData',
            field=models.ForeignKey(to='medicaldata.MedicalData'),
        ),
    ]
