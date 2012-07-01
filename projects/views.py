from django.shortcuts import render_to_response
from django.template import RequestContext

from projects.models import Project

def index(request):
    projects = Project.objects.all()
    data = {'projects': projects}
    context = RequestContext(request)
    return render_to_response('projects/project_list.html', data, context)
