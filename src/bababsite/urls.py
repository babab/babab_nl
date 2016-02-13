from django.conf.urls import include, url
from django.contrib import admin

from bababblog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^project/(?P<project_name>[\w-]+)/$', views.project, name='project'),
    url(r'^blog/(?P<article_url>[\w-]+)/$', views.article, name='article'),

    url(r'^admin/', include(admin.site.urls)),
]
