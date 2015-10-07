# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_shariff', '0010_auto_20151001_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='orientation_choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orientation_choices', models.CharField(default=b'horizontal', max_length=2, choices=[(b'vertical', b'vertical'), (b'horizontal', b'horizontal')])),
            ],
        ),
    ]
