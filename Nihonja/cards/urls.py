from .views import index, review
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<pk>\d+)/$', review, name='review'),
]
