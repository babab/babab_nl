from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'tools.views.index', name='index'),
)
