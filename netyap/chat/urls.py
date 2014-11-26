__author__ = 'kabraadit'

from django.conf.urls import patterns, include, url
from chat import views

urlpatterns = patterns('',
    url(r'^joinchat/(\d+)$', views.joinChatroom, name='joinChatroom'),
    url(r'^(\d+)$', views.index, name='index'),
    #url(r'^addMsg$', views.addMsg, name='addMsg')

)
