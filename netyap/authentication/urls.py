__author__ = 'dheerendra'

from django.conf.urls import patterns, include, url
from auth import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'netyap.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.authentication, name='authentication'),
)
