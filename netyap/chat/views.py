from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from forms import createChatroomForm
from models import chatroom


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
            chatroom.title = title
            chatroom.instructor_name = prof
            chatroom.course_id = course_id
            chatroom.save()

            return startChat(request)

        else:
            print(form.errors)

    else:
        form = createChatroomForm()


def joinChatroom(request,chatroom_id):

    context = RequestContext(chatroom_id)



def startChat():
    return 0