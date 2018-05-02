from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list/$', views.index),
    url(r'^vote/(?P<pollid>[0-9]+)',views.vote),
    url(r'^view/(?P<pollid>[0-9]+)', views.view),
    url(r'^detail/(?P<pollid>[0-9]+)',views.detail),
]