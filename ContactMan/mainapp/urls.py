from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new, name = 'new'),
    url(r'post_url/$', views.post_contact, name='post_contact'),
    url(r'^(?P<contact_id>[0-9]+)/edit/$', views.edit, name = 'edit'),
    url(r'^(?P<contact_id>[0-9]+)/$', views.detail, name='detail')
]