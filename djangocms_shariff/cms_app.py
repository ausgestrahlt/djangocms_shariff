from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from django.conf import settings


class ShariffBackendApphook(CMSApp):
    name = "Shariff-Backend"
    urls = ["apps.djangocms_shariff.urls"]
    app_name = 'shariff_backend'


if getattr(settings, 'CMS_SHARIFF_REGISTER_APPHOOK', False):
    apphook_pool.register(ShariffBackendApphook)
