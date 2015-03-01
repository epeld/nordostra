from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.models import User

import datetime

from attendance.models import Session

# Create your views here.

def past_sessions(request):
    num_users = User.objects.count()
    sessions = Session.objects.filter(date__lte=datetime.date.today()).order_by("-date")
    coming = Session.objects.filter(date__gt=datetime.date.today()).order_by("-date")
    env = { 'sessions': sessions, 'user': request.user, 'num_users': num_users, 'coming': coming }
    return render_to_response('jade/sessions.jade', env)
