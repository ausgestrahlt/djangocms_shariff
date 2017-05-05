# -*- coding: utf-8 -*-

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from models import Shariff
from django.utils.translation import ugettext_lazy as _


class ShariffPlugin(CMSPluginBase):
    name = 'Shariff'
    render_template = 'djangocms_shariff/_plugin.html'
    model = Shariff
    fieldsets = (
        (_('General'), {
            'fields': [
                'use_backend', 'orientation_choices', 'theme_choices', 'info'
                ]
            }),
        (_('Social Media'), {
            'fields': [
                'addthis',
                'facebook',
                'googleplus',
                'linkedin',
                'pinterest',
                'threema',
                'tumblr',
                'twitter',
                'whatsapp',
                'xing',
                ]
            }),
        ('E-mail', {
            'fields': ['mail', 'mail_subject', 'mail_body']
            }),
    )

    def render(self, context, instance, placeholder):
        context = super(ShariffPlugin, self)\
                .render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(ShariffPlugin)
