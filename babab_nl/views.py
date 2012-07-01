from django.shortcuts import render_to_response
from django.template import RequestContext

from news.models import NewsItem

def index(request):
    news = NewsItem.objects.all().order_by('-time')[:5]
    data = {'news': news}
    context = RequestContext(request)
    return render_to_response('home.html', data, context)
