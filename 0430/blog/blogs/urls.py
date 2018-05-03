from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.blog),
    url(r'^post/$', views.post),
    url(r'^delete/(?P<poid>[0-9]+)$', views.delpost),
    url(r'^edit/(?P<poid>[0-9]+)$', views.editpost),
]