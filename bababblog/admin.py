from django.contrib import admin

from bababblog import models


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title', )}


admin.site.register(models.Tag)
admin.site.register(models.Comment)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Project)
