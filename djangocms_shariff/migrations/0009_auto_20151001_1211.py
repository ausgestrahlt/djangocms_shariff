# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_shariff', '0008_auto_20151001_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shariff',
            name='email_body',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='shariff',
            name='email_subject',
            field=models.TextField(blank=True),
        ),
    ]
