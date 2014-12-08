__author__ = 'haohan'
from django.conf.urls.defaults import *
from views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dota2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^dashboard/',dashboard,{'template_name':'index_home.html'}),
    url(r'^profile/',profile,{'template_name':'profile.html'}),
    url(r'^table/',dashboard,{'template_name':'tables.html'}),
    url(r'^form/',dashboard,{'template_name':'forms.html'}),
    url(r'^blank-page/',dashboard,{'template_name':'time.html'}),
    url(r'^bootstrap-grid/',second,{'template_name':'report.html'}),
    url(r'^bootstrap-elements/',dashboard,{'template_name':'bootstrap-elements.html'}),
)

