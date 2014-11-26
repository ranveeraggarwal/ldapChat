from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from chat.models import Chatroom, Notice

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
            notice = Notice.objects.filter(chatroom_id__instructor_username=ins_data['username']).order_by('time_stamp')[0]
        except IndexError:
            notice = None
        #chatroom = notice.chatroom.title
        #ins_data['notice']
        return render_to_response('instructor/instructor_home.html', ins_data, context)
    elif userType == 's':
        redirect('/student')
    else:
        redirect('/')