from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'Nihonja.core.views.home', name='home'),
    url(r'^contact/$', 'Nihonja.core.views.contact', name='contact'),
]
