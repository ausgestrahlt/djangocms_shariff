# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_shariff', '0005_shariff_twitter'),
    ]

    operations = [
        migrations.AddField(
            model_name='shariff',
            name='emailadress',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shariff',
            name='emailboolean',
            field=models.BooleanField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shariff',
            name='emailsubject',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
