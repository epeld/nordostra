from django.http import HttpResponse
from django.shortcuts import render_to_response

from news.models import NewsItem


# TODO serve these things by a faster web server!
def index(request):
    n = NewsItem.objects.order_by("-date")[:5]
    return render_to_response('jade/index.jade', {'news': n, 'user': request.user})

def enlist(request):
    return render_to_response('jade/enlist.jade', {'user': request.user})

def styles(request):
    return render_to_response('styles/style.css', {'user': request.user})
