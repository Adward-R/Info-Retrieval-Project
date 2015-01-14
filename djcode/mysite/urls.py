from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import *

import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', search_form),
    url(r'^search-form/$', search_form),
    url(r'^search-form-basic/$', search_form_basic),
    url(r'^wordcloud/$',wordcloud),
    url(r'^bubble/$',bubble),
    url(r'^search/$',search),
    url(r'^search-basic/$',search_basic),
    url(r'^editor/$',directed_graph_editor),
    url(r'^pok-timeline/$',pok_timeline),
    url(r'^event-timeline/$',event_timeline),
    url(r'^paper-total/$',paper_total),
    url(r'^paper-frequency/$',paper_frequency),
    url(r'^newspaper-relation/$',newspaper_relation),
    url(r'^email-relation/$',email_relation),
    url(r'^pok-org/$',pok_org),
    url(r'^final-timeline/$',final_timeline),
    url( r'^static/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root':settings.STATIC_URL }),
    #url(r'^admin/', include(admin.site.urls)),
)
