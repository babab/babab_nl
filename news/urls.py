from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'news.views.index', name='index'),
)
