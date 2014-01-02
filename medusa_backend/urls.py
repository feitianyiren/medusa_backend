from django.conf.urls import patterns, include, url
from django.contrib import admin

from soplog.views import *
#from django.conf.urls.defaults import *

admin.autodiscover()

urlpatterns = patterns('',
                        url(r'^admin/', include(admin.site.urls)),
                        url(r'^checklist/$', checkList),
                        url(r'^checklist/groupid/(\d*)/$', checklistSearchByGroup),   
                        url(r'^checklist/checklistid/(\d*)/$', checklistSteps), 
                        #url(r'^uploadTest/%', uploadTest),                   
)





#url(r'^$', homepage),

    # Examples:
    # url(r'^$', 'medusa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#     url(r'^hello/$',hello),
    #url(r'^hello/', 'medusa.views.hello', name='hello'),
#     url(r'^time/$', currentTime),
    
#     url(r'^time/plus/(\d{1,2})/$', hoursAhead),
#     url(r'^name/([^/]+)/$', myName),
#     url(r'^template/([^/]+)/$', template),
    
    #url(r'^login/$')
#     url(r'^test/$',test),
    
 
