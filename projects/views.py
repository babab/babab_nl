from django.shortcuts import render_to_response

from projects.models import Project

def index(request):
    projects = Project.objects.all()
    r = {'projects': projects}
    return render_to_response('projects/project_list.html', r)
