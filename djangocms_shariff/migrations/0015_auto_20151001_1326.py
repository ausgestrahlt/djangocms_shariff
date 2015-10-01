# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_shariff', '0014_shariff_theme_choises'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shariff',
            name='orientation_choices',
            field=models.CharField(default=b'horizontal', max_length=10, choices=[(b'vertical', b'vertical'), (b'horizontal', b'horizontal')]),
        ),
        migrations.AlterField(
            model_name='shariff',
            name='theme_choises',
            field=models.CharField(default=b'standard', max_length=8, choices=[(b'standard', b'standard'), (b'grey', b'grey'), (b'white', b'white')]),
        ),
    ]
