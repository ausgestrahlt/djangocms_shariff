# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_shariff', '0018_auto_20151001_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shariff',
            name='orientation_choices',
            field=models.CharField(default=b'horizontal', max_length=10, verbose_name='orientation', choices=[(b'vertical', 'vertical'), (b'horizontal', 'horizontal')]),
        ),
    ]
