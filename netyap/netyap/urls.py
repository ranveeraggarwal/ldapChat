from django.conf.urls import patterns, include, url
from authentication.urls import url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'netyap.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^authentication/', include('authentication.urls')),
)
