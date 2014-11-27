from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from models import Chatroom, Notice
from models import SubscriberTable
from models import Chat

def index(request, roomno):
    session = request.session
    context = RequestContext(request)
    theChatRoom = Chatroom.objects.all().filter(pk = roomno)[0]
    context_dict = {'room_title': theChatRoom.title, 'course_name': theChatRoom.course_id, 'user_name': session.get('name'), 'instructor': theChatRoom.instructor_name}
    return render_to_response('chat/chatroom.html', context_dict, context)

def joinChatroom(request,chatroom_id):

    context = RequestContext(request)
    session = request.session
    user_id = session.get('username')
    theChatRoom = Chatroom.objects.all().filter(chatroom_id=chatroom_id)[0]
    theBroadcast = Notice.objects.all().filter(chatroom_id=chatroom_id).order_by("-pk")[0:15]
    chat_data = {'isSubChatRoom':0,'room_title': theChatRoom.title, 'course_name': theChatRoom.course_id, 'user_name': session.get('name'), 'instructor': theChatRoom.instructor_name}
    chat_data['broadcasts'] = theBroadcast
    subscribe= SubscriberTable(
                chatroom_id=theChatRoom,
                user_id=user_id,
            )
    subscribe.save()
    #chat_data={}
    chat_data['data']=Chat.objects.filter(chatroom_id=chatroom_id).order_by('-time_stamp')
    return render_to_response('chat/chatroom.html',chat_data, context)

def leaveroom(request,chatroom_id):

    context = RequestContext(request)
    session = request.session
    user_id = session.get('username')
    instance = SubscriberTable.objects.filter(chatroom_id=chatroom_id).filter(user_id = user_id).delete()
    #instance.delete()
    return redirect('/')

def joinSubChatroom(request,chatroom_id,chat_id):

    context = RequestContext(request)
    session = request.session
    chat_data = Chat.objects.filter(chatroom_id=chatroom_id, chat_id=chat_id)[0]
    chatroom_data = Chatroom.objects.filter(chatroom_id=chatroom_id)[0]
    #user_id = session.get('username')
    chat = {'isSubChatRoom':1,'chatroom_id':chatroom_id, 'chat_id':chat_id, 'message':chat_data.message,
            'room_title':chatroom_data.title, 'instructor':chatroom_data.instructor_name,
            'course_name':chatroom_data.course_id, 'parent_user_id':chat_data.user_id}
    return render_to_response('chat/chatroom.html',chat,context)









