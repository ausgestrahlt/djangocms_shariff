# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_shariff', '0017_auto_20151001_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shariff',
            name='email',
            field=models.BooleanField(help_text=b'Enable sharing via e-mail'),
        ),
    ]
