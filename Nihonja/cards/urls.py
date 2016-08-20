from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^$', 'Nihonja.cards.views.index', name='index'),
    url(r'^(?P<pk>\d+)/$', 'Nihonja.cards.views.review', name='review'),
]
