from django.conf.urls import include, url
from Nihonja.cards.views import index, review

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<slug>[\w_-]+)/$', review, name='review'),
]
