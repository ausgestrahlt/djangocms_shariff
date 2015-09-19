# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_shariff', '0004_auto_20150918_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='shariff',
            name='twitter',
            field=models.BooleanField(default=''),
            preserve_default=False,
        ),
    ]
