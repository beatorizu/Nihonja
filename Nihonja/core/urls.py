from .views import contact, home
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^contact/$', contact, name='contact'),
]
