from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class ShariffBackendApphook(CMSApp):
    name = "Shariff-Backend"
    urls = ["apps.djangocms_shariff.urls"]
    app_name = 'shariff_backend'


apphook_pool.register(ShariffBackendApphook)
