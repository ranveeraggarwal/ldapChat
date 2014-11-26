__author__ = 'kabraadit'

from django.conf.urls import patterns, include, url
from chat import views

urlpatterns = patterns('',
    url(r'^createchat$', views.createChatroom, name='createChatroom'),
    url(r'^joinchat/(\d+)$', views.joinChatroom, name='joinChatroom'),
)
