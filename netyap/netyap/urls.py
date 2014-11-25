from django.conf.urls import patterns, include, url
from authentication.urls import url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'netyap.views.sample-app', name='sample-app'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('authentication.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
