# -*- coding: utf-8 -*-

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from cms.models import CMSPlugin
from django.contrib import admin

from models import Shariff

class ShariffPlugin(CMSPluginBase):
    name = 'Shariff'
    module = 'ausgestrahlt'
    render_template = 'djangocms_shariff/_plugin.html'
    model = Shariff 
    fieldsets = (
        ('general', {
            'fields': ['use_backend',]
            }),
        (None, {
            'fields': ['facebook','twitter']
            }),
        (None, {
            'fields': ['emailboolean','emailadress','emailsubject']
            }),
    )

plugin_pool.register_plugin(ShariffPlugin)
