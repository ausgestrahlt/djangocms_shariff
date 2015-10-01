# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_shariff', '0013_auto_20151001_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='shariff',
            name='theme_choises',
            field=models.CharField(default=b'standard', max_length=2, choices=[(b'standard', b'standard'), (b'grey', b'grey'), (b'white', b'white')]),
        ),
    ]
