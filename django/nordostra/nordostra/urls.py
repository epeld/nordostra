from django.conf.urls import patterns, include, url
from django.contrib import admin

import attendance.urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nordostra.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'nordostra.views.index', name='index'),
    url(r'^enlist', 'nordostra.views.enlist', name='enlist'),

    url(r'^main.css', 'nordostra.views.styles', name='styles'),

    url(r'^narvaro/', include(attendance.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
