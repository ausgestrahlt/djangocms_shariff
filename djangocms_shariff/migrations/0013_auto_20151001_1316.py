# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_shariff', '0012_auto_20151001_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shariff',
            name='info',
            field=models.BooleanField(default=False, help_text=b'Info about the Plugin'),
        ),
    ]
