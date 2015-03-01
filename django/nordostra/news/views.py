from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.models import User

from news.models import NewsItem

def index(request):
    news = NewsItem.objects.order_by("-date")
    env = {'news': news}
    return render_to_response('jade/news.jade')
