# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [("cms", "0012_auto_20150607_2207")]

    operations = [
        migrations.CreateModel(
            name="Shariff",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        on_delete=models.deletion.CASCADE,
                        parent_link=True,
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        to="cms.CMSPlugin",
                    ),
                ),
                (
                    "use_backend",
                    models.BooleanField(
                        default=False, verbose_name="Use the shariff backend"
                    ),
                ),
                (
                    "orientation_choices",
                    models.CharField(
                        default=b"horizontal",
                        max_length=10,
                        verbose_name="orientation",
                        choices=[
                            (b"vertical", "vertical"),
                            (b"horizontal", "horizontal"),
                        ],
                    ),
                ),
                (
                    "theme_choices",
                    models.CharField(
                        default=b"standard",
                        max_length=8,
                        verbose_name="theme",
                        choices=[
                            (b"standard", "standard"),
                            (b"grey", "grey"),
                            (b"white", "white"),
                        ],
                    ),
                ),
                ("facebook", models.BooleanField(default=False)),
                ("twitter", models.BooleanField(default=False)),
                ("googleplus", models.BooleanField(default=False)),
                ("linkedin", models.BooleanField(default=False)),
                ("pinterest", models.BooleanField(default=False)),
                ("xing", models.BooleanField(default=False)),
                ("whatsapp", models.BooleanField(default=False)),
                ("addthis", models.BooleanField(default=False)),
                ("tumblr", models.BooleanField(default=False)),
                (
                    "info",
                    models.BooleanField(
                        default=False, help_text="Provide information about the Plugin"
                    ),
                ),
                ("mail", models.BooleanField(help_text="Enable sharing via e-mail")),
                ("mail_subject", models.TextField(verbose_name="subject", blank=True)),
                ("mail_body", models.TextField(verbose_name="content", blank=True)),
            ],
            options={"abstract": False},
            bases=("cms.cmsplugin",),
        )
    ]
