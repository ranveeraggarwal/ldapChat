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
        student_data['chatrooms']=showchat(student_data['username'])
        student_data['subs_chatrooms'] = showSubscribedChat(student_data['username'])
        student_data['broadcasts'] = showbroadcasts(student_data['username'])
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
    all_chat = Chatroom.objects.all().exclude(subscribertable__user_id = userid).order_by("-time_stamp")
    return all_chat

def showSubscribedChat(userid):
    subs_chat = Chatroom.objects.all().filter(subscribertable__user_id=userid).order_by("-time_stamp")
    return subs_chat

def showbroadcasts(userid):
    return Notice.objects.all().filter(chatroom_id__subscribertable__user_id=userid).order_by("-time_stamp")