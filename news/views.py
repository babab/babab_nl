from django.shortcuts import render_to_response
from django.template import RequestContext

from news.models import NewsItem

def index(request):
    news = NewsItem.objects.all().order_by('-time')
    data = {'news': news}
    context = RequestContext(request)
    return render_to_response('news/news_list.html', data, context)
