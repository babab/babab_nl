from django.contrib import admin

from projects.models import Project, ProjectRelease, ProjectTag

admin.site.register(Project)
admin.site.register(ProjectRelease)
admin.site.register(ProjectTag)
