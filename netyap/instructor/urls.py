__author__ = 'ranveer'

from django.conf.urls import patterns, include, url
from instructor import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)