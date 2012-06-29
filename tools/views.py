from django.shortcuts import render_to_response
import tools

def index(request):
    r = {'tools': tools.tools}
    return render_to_response('tools/index.html', r)

def rot13(request):
    if request.GET:
        r = {'text': request.GET['text'].encode('rot13') }
    else:
        r = {'text': ''}

    return render_to_response('tools/rot13.html', r)
