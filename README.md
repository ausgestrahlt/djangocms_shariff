# djangoCMS shariff

## A django and djangoCMS implementation of [shariff](https://github.com/heiseonline/shariff)

Provides a shariff plugin for [djangoCMS](https://github.com/divio/django-cms) >= 3.0 and a django app (with djangoCMS app hook) for the [shariff backend](https://github.com/heiseonline/shariff#backends).

This is work in progress.

### Configurable apphook

The apphook for the shariff backend can be registered by setting ``CMS_SHARIFF_REGISTER_APPHOOK`` to ``True`` in your ``settings.py``.

If you want to use the backend but don't want an apphook, just include this module's urls in your ``urls.py`` like e.g. so:

```
url(r'^shariff-backend-url/', include('djangocms_shariff.urls', namespace='shariff_backend')),
```
