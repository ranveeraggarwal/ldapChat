__author__ = 'ranveer'

from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^index$', views.index, name='index'),
)
