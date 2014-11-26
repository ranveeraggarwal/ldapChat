from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from chat.models import Chatroom, Notice
from chat.models import SubscriberTable
from chat.models import Chat
from chat.forms import createChatroomForm

# Create your views here.

def index(request):
    session = request.session
    context = RequestContext(request)
    userType = request.session.get('userType')
    ins_data = {}
    if userType == 'f':
        ins_data['instructor_name'] = session.get('name')
        ins_data['username'] = session.get('username')
        instructor_chatrooms = Chatroom.objects.filter(instructor_username=ins_data['username'])
        ins_data['chatroom'] = instructor_chatrooms
        try:
            notice = Notice.objects.filter(chatroom_id__instructor_username=ins_data['username']).order_by('time_stamp')[5]
        except IndexError:
            notice = None
        #chatroom = notice.chatroom.title
        #ins_data['notice']
        return render_to_response('instructor/instructor_home.html', ins_data, context)
    elif userType == 's':
        return redirect('/student')
    else:
        return redirect('/')

def createChatroom(request):

    context = RequestContext(request)

    if request.method == 'POST':
        form = createChatroomForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            title = createChatroomForm.objects.get(name='Title')
            prof= createChatroomForm.objects.get(name='Prof_Name')
            course_id= createChatroomForm.objects.get(name='Course_ID')
            Chatroom.title = title
            Chatroom.instructor_name = prof
            Chatroom.course_id = course_id
            Chatroom.save()

            return startChat(request)

        else:
            print(form.errors)
            return startChat(request)
    else:
        form = createChatroomForm()
    return render_to_response('chat/' + str(1) + '.html',{}, context)

def startChat():
    return 0