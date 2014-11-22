__author__ = 'dheerendra'

from django.conf.urls import patterns, include, url
from authentication import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'netyap.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^login', views.authentication, name='login'),
)
