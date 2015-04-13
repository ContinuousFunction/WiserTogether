# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicaldata', '0003_auto_20150407_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='medicalData',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
