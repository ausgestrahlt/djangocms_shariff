from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.DataBackendView.as_view(), name='get'),
)
