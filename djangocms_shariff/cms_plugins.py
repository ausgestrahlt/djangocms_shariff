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
        ('General', {
            'fields': ['use_backend','orientation_choices','theme_choices']
            }),
        ('Services', {
            'fields': ['facebook','twitter', 'googleplus', 'linkedin', 'pinterest', 'xing', 'whatsapp', 'addthis', 'tumblr', 'info']
            }),
        ('E-mail', {
            'fields': ['email','email_subject','email_body']
            }),
    )

plugin_pool.register_plugin(ShariffPlugin)
