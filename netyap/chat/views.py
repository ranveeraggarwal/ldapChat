from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from forms import createChatroomForm
from models import Chatroom
from models import SubscriberTable
from models import Chat

def index(request):
    context = RequestContext(request)

    context_dict = {'boldMessage': "I am bold font from the context"}

    return render_to_response('chat/chatroom.html', context_dict, context)

def createChatroom(request):

    context = RequestContext(request)

    if request.method == 'POST':
        form = createChatroomForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            title = createChatroomForm.objexts.get(name='Title')
            prof= createChatroomForm.objexts.get(name='Prof_Name')
            course_id= createChatroomForm.objexts.get(name='Course_ID')
            Chatroom.title = title
            Chatroom.instructor_name = prof
            Chatroom.course_id = course_id
            Chatroom.save()

            return startChat(request)

        else:
            print(form.errors)

    else:
        form = createChatroomForm()

def startChat():
    return 0

def joinChatroom(request,chatroom_id):

    context = RequestContext(request)
    session = request.session
    user_id = session.get('userId')
    subscribe=subscribertable(
                chatroom_id=chatroom_id,
                user_id=user_id,
            )
    chat_data = chat.objects.filter(chatroom_id=chatroom_id)
    return render_to_response('chat/chatroom.html',chat_data, context)

    subscribe.save()
