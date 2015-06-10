from django.shortcuts import render_to_response
from django.template import RequestContext

from bababblog import models


def view(request, template, data={}):
    '''Shortcut view return function with RequestContext'''
    return render_to_response(
        template, data, context_instance=RequestContext(request)
    )


def index(request):
    latest = models.Article.objects.latest()
    data = {'latest': latest}
    return view(request, 'index.html', data)
