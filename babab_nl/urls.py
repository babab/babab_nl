from django.conf.urls import patterns, include, url
from django.contrib import admin

import babab_nl.views
import news.urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'babab_nl.views.index', name='index'),
    url(r'^news/$', include(news.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
