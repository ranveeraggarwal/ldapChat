__author__ = 'kabraadit'

from django.conf.urls import patterns, include, url
from chat import views

urlpatterns = patterns('',
    #url(r'^joinchat/(\d+)$', views.joinChatroom, name='joinChatroom'),
    url(r'^(\d+)$', views.joinChatroom, name='index'),
    url(r'^leaveroom/(\d+)$',views.leaveroom, name='leaveroom'),
    #url(r'^addMsg$', views.addMsg, name='addMsg')

)
