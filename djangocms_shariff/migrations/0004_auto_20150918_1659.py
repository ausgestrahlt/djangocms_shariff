# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_shariff', '0003_auto_20150918_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shariff',
            name='facebook',
            field=models.BooleanField(),
        ),
    ]
