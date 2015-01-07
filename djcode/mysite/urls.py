from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import *

import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^search-form/$', search_form),
    url(r'^search/$',search),
    url( r'^static/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root':settings.STATIC_URL }),
    #url(r'^admin/', include(admin.site.urls)),
)
