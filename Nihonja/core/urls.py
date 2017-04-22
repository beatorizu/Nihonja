from django.conf.urls import include, url
from django.contrib import admin
from Nihonja.core.views import home, contact

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^contact/$', contact, name='contact'),
]
