from django.contrib import admin

from news.models import NewsItem, NewsTag

admin.site.register(NewsItem)
admin.site.register(NewsTag)
