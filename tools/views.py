from django.shortcuts import render_to_response
import tools

def index(request):
    r = {'tools': tools.tools}
    return render_to_response('tools/index.html', r)
