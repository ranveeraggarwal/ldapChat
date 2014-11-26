from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.
from chat.models import Chatroom, Notice


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
        student_data['broadcasts'] = showbroadcasts(student_data['userId'])
        theCourses = []
        for oneRoom in student_data['chatrooms']:
            if oneRoom.course_id in theCourses:
                pass
            else:
                theCourses.append(oneRoom.course_id)
        student_data['access_level']="Student"
        student_data['courses'] = theCourses

    return render_to_response('student/student_home.html',student_data, context)

def showchat(userid):
    return Chatroom.objects.all()

def showbroadcasts(userid):
    return Notice.objects.all()