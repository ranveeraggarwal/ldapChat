__author__ = 'kabraadit'

from django.conf.urls import patterns, include, url
from chat import views

urlpatterns = patterns('',
    #url(r'^joinchat/(\d+)$', views.joinChatroom, name='joinChatroom'),
    url(r'^(\d+)$', views.joinChatroom, name='index'),
    url(r'^(\d+)\/(\d+)$', views.joinSubChatroom, name='index'),
    url(r'^leaveroom/(\d+)$',views.leaveroom, name='leaveroom'),
    url(r'^getChatroomDetail/(\d+)$', views.getChatroomDetail, name='getChatRoomDetails'),
    #url(r'^addMsg$', views.addMsg, name='addMsg')

)
