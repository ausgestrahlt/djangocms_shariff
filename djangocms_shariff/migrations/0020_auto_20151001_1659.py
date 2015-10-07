# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_shariff', '0019_auto_20151001_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shariff',
            name='theme_choices',
            field=models.CharField(default=b'standard', max_length=8, verbose_name='theme', choices=[(b'standard', 'standard'), (b'grey', 'grey'), (b'white', 'white')]),
        ),
    ]
