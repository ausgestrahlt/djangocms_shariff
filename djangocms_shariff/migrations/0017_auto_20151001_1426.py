# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_shariff', '0016_auto_20151001_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shariff',
            old_name='theme_choises',
            new_name='theme_choices',
        ),
    ]
