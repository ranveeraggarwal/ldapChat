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
            new_data = form.save(commit = True)
            room_no = new_data.pk
            return startChat(request, room_no)
        else:
            print(form.errors)
    else:
        form = createChatroomForm()

def startChat(request, room_no):
    return redirect('/chat/'+str(room_no))
