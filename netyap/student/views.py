from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.
from chat.models import Chatroom


def index(request):
    session = request.session
    context = RequestContext(request)
    type = request.session.get('userType')
    student_data = {}
    if type == 's':
        student_data['student_name'] = session.get('name')
        student_data['username'] = session.get('username')
        student_data['userId']=session.get('userId')
        student_data['chatrooms']=showchat(student_data['userId'])
        student_data['access_level']="Student"

    return render_to_response('student/student_home.html',student_data, context)

def showchat(userid):
    return Chatroom.objects.all()

