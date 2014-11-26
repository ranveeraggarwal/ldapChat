from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from chat.models import chatroom

# Create your views here.

def index(request):
    session = request.session
    context = RequestContext(request)
    userType = request.session.get('userType')
    ins_data = {}
    if userType == 'f':
        ins_data['name'] = session.get('name')
        ins_data['username'] = session.get('username')
        instructor_chatrooms = chatroom.objects.filter(instructor_username = ins_data['username'])
        ins_data['chatroom'] = instructor_chatrooms
        return render_to_response('instructor/instructor_home.html', ins_data, context)
    elif userType == 's':
        redirect('/student')
    else:
        redirect('/')