from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from forms import createChatroomForm
from models import chatroom


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
            chatroom.prof = prof
            chatroom.course_id = course_id
            chatroom.save()

            return startChat(request)

        else:
            print(form.errors)

    else:
        form = createChatroomForm()

    return render_to_response('chat/index.html', {'form':form}, context)

def startChat():
    return 0