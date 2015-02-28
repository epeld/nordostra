from django.http import HttpResponse
from django.shortcuts import render_to_response

# TODO serve these things by a faster web server!
def index(request):
    return render_to_response('jade/index.jade', {})

def enlist(request):
    return render_to_response('jade/enlist.jade', {})

def styles(request):
    return render_to_response('styles/style.css', {})
