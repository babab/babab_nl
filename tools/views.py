from django.shortcuts import render_to_response
from django.template import RequestContext
import tools

def index(request):
    data = {'tools': tools.tools}
    context = RequestContext(request)
    return render_to_response('tools/index.html', data, context)

def rot13(request):
    if request.POST:
        data = {'text': request.POST['text'].encode('rot13') }
    else:
        data = {'text': ''}

    context = RequestContext(request)
    return render_to_response('tools/rot13.html', data, context)
