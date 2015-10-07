# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_shariff', '0011_orientation_choice'),
    ]

    operations = [
        migrations.DeleteModel(
            name='orientation_choice',
        ),
        migrations.AddField(
            model_name='shariff',
            name='orientation_choices',
            field=models.CharField(default=b'horizontal', max_length=2, choices=[(b'vertical', b'vertical'), (b'horizontal', b'horizontal')]),
        ),
    ]
