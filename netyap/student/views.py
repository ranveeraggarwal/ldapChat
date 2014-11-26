from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.
from chat.models import chatroom


def index(request):
    session = request.session
    context = RequestContext(request)
    type = request.session.get('userType')
    student_data = {}
    if type == 's':
        student_data['name'] = session.get('name')
        student_data['username'] = session.get('username')
        student_data['userId']=session.get('userId')
        student_data['chat-old']=showchat(student_data['userId'])

    return render_to_response('student/student_home.html',student_data, context)

def showchat(userid):
    return chatroom.objects.all()

