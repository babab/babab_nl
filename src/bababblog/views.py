from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

from bababblog import models


def view(request, template, data={}):
    '''Shortcut view return function with RequestContext'''
    return render_to_response(
        template, data, context_instance=RequestContext(request)
    )


def defaultview(request, template, extra_data={}):
    '''Generic shortcut view function with projects and articles'''
    articles = models.Article.objects.all()
    projects = models.Project.objects.all().order_by('ordering')
    data = {'articles': articles, 'projects': projects}
    if extra_data:
        data.update(extra_data)
    return view(request, template, data)


def index(request):
    try:
        data = {'latest': models.Article.objects.latest()}
        return defaultview(request, 'index.html', data)
    except models.Article.DoesNotExist:
        return defaultview(request, 'index.html')


def project(request, project_name):
    try:
        data = {'project': models.Project.objects.get(name=project_name)}
    except models.Project.DoesNotExist:
        data = {'project': None}
        raise Http404('Project {} does not exist'.format(project_name))
    return defaultview(request, 'project.html', data)
