#from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
import views
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from settings import *
urlpatterns = patterns('',
(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    #url(r'^$', include("index.html")),
    url(r'', include('recengine.login.urls')),
    url(r'^app1/', include('recengine.app1.url')),
    url(r'^hits/',views.bia),
    url(r'^d3/',views.d3),
    url(r'^network/',views.net3),
    url(r'^us-map/',views.map),
    url(r'^rfm/',views.rfm),
    url(r'^stock/',views.stock),
    url(r'^chutu/',views.chutu),
    url(r'^about/',views.about),
    url(r'^home/',views.home_1),
    url(r"^prediction/",views.prediction),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:  
   urlpatterns += patterns('', 
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),   
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}), 
    )  