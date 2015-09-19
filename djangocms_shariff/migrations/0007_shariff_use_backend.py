# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_shariff', '0006_auto_20150918_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='shariff',
            name='use_backend',
            field=models.BooleanField(default=False),
        ),
    ]
