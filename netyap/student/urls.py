__author__ = 'kabraadit'

from django.conf.urls import patterns, include, url
from student import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #url(r'^student_home.html', stude)
)