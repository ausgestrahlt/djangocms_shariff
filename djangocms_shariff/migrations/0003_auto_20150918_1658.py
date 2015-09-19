# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_shariff', '0002_shariff_caption_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shariff',
            name='caption_text',
        ),
        migrations.RemoveField(
            model_name='shariff',
            name='title',
        ),
        migrations.AddField(
            model_name='shariff',
            name='facebook',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
