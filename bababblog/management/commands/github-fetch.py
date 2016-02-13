import json

from django.core.management.base import BaseCommand
from django.conf import settings

from bababblog.models import Project
from bababblog.lib import GithubApi


class Command(BaseCommand):
    help = 'Fetch project READMEs from Github and update in database'

    # def add_arguments(self, parser):
    #     parser.add_argument('project_name', nargs='+', type=int)

    def handle(self, *args, **options):
        api = GithubApi(username=settings.GITHUB_USERNAME,
                        ignore=settings.PROJECTS_IGNORE_LIST, throttle=False)
        api.getRepos()

        counter = 1
        for item in api.repos:
            self.stdout.write('Downloading README of {}'.format(item['name']))

            try:
                project = Project.objects.get(name=item['name'])
            except Project.DoesNotExist:
                project = Project(name=item['name'])

            project.language = item['language']
            project.homepage = item['homepage']
            project.description = item['description']
            project.ordering = counter
            project.html = api.getReadmeContent(item['name'])
            project.json = json.dumps(item)
            project.save()

            if api.throttle and counter == 3:
                break
            counter += 1
