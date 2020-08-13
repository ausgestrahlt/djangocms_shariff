# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("djangocms_shariff", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="shariff",
            name="threema",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="shariff",
            name="cmsplugin_ptr",
            field=models.OneToOneField(
                on_delete=models.deletion.CASCADE,
                parent_link=True,
                related_name="djangocms_shariff_shariff",
                auto_created=True,
                primary_key=True,
                serialize=False,
                to="cms.CMSPlugin",
            ),
        ),
        migrations.AlterField(
            model_name="shariff",
            name="info",
            field=models.BooleanField(
                default=False, help_text="Show info icon next to share buttons"
            ),
        ),
        migrations.AlterField(
            model_name="shariff",
            name="use_backend",
            field=models.BooleanField(
                default=False,
                help_text="The backend will fetch sharing statistics for the respective channels",
                verbose_name="Use the shariff backend",
            ),
        ),
    ]
