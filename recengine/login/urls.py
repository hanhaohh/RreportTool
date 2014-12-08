from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from views import *
admin.autodiscover()
        
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loginsesion.views.home', name='home'),
    # url(r'^loginsesion/', include('loginsesion.foo.urls')),
        
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        
    # Uncomment the next line to enable the admin:
    url(r'^regist/$', regist),
    url(r'^login/$', login),
    url(r'^index/$', index),
    url(r'^logout/$',user_logout),
)
