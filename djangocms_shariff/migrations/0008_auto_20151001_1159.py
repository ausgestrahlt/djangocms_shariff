# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_shariff', '0007_shariff_use_backend'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shariff',
            old_name='emailboolean',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='shariff',
            old_name='emailsubject',
            new_name='email_body',
        ),
        migrations.RemoveField(
            model_name='shariff',
            name='emailadress',
        ),
        migrations.AddField(
            model_name='shariff',
            name='email_subject',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shariff',
            name='use_backend',
            field=models.BooleanField(default=False, verbose_name='Use the shariff backend'),
        ),
    ]
