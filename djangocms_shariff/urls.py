from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.DataBackendView.as_view(), name='get'),
]
