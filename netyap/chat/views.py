from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from forms import createChatroomForm
from models import Chatroom
from models import SubscriberTable
from models import Chat

def index(request, roomno):
    context = RequestContext(request)

    context_dict = {'boldMessage': "I am bold font from the context"}

    return render_to_response('chat/chatroom.html', context_dict, context)

def joinChatroom(request,chatroom_id):

    context = RequestContext(request)
    session = request.session
    user_id = session.get('userId')
    subscribe= SubscriberTable(
                chatroom_id=chatroom_id,
                user_id=user_id,
            )
    subscribe.save()
    chat_data = Chat.objects.filter(chatroom_id=chatroom_id)
    return render_to_response('chat/chatroom.html',chat_data, context)




