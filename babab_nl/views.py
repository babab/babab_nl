from django.shortcuts import render_to_response

from news.models import NewsItem

def index(request):
    news = NewsItem.objects.all().order_by('-time')[:5]
    r = {'news': news,}
    return render_to_response('home.html', r)
