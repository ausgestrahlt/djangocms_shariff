# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_shariff', '0009_auto_20151001_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='shariff',
            name='addthis',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shariff',
            name='googleplus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shariff',
            name='info',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shariff',
            name='linkedin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shariff',
            name='pinterest',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shariff',
            name='tumblr',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shariff',
            name='whatsapp',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shariff',
            name='xing',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='shariff',
            name='facebook',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='shariff',
            name='twitter',
            field=models.BooleanField(default=False),
        ),
    ]
