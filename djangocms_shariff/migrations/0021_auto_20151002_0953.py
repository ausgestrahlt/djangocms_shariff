# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_shariff', '0020_auto_20151001_1659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shariff',
            old_name='email',
            new_name='mail',
        ),
        migrations.RemoveField(
            model_name='shariff',
            name='email_body',
        ),
        migrations.RemoveField(
            model_name='shariff',
            name='email_subject',
        ),
        migrations.AddField(
            model_name='shariff',
            name='mail_body',
            field=models.TextField(verbose_name='content', blank=True),
        ),
        migrations.AddField(
            model_name='shariff',
            name='mail_subject',
            field=models.TextField(verbose_name='subject', blank=True),
        ),
    ]
