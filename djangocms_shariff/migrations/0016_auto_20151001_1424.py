# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_shariff', '0015_auto_20151001_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shariff',
            name='email',
            field=models.BooleanField(help_text=b'Enable share via e-mail'),
        ),
        migrations.AlterField(
            model_name='shariff',
            name='info',
            field=models.BooleanField(default=False, help_text=b'Provide information about the Plugin'),
        ),
    ]
