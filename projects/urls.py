from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'projects.views.index', name='index'),
)
