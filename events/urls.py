from django.conf.urls import url

from . import views

app_name = 'events'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.event_detail, name='event_detail'),
    url(r'^(?P<id>[0-9]+)/edit/$', views.event_update, name='event_update'),
]