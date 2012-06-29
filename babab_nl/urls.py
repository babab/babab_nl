from django.conf.urls import patterns, include, url
from django.contrib import admin

import news.urls
import projects.urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'babab_nl.views.index', name='index'),
    url(r'^news/$', include(news.urls)),
    url(r'^projects/$', include(projects.urls)),
    url(r'^tools/$', 'tools.views.index', name='tools_index'),
    url(r'^rot13/$', 'tools.views.rot13', name='rot13'),
    url(r'^admin/', include(admin.site.urls)),
)
