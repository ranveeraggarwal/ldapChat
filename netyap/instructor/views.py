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
        instructor_chatrooms = Chatroom.objects.filter(instructor_username=ins_data['username']).order_by("-pk")
        ins_data['chatroom'] = instructor_chatrooms
        theCourses = []
        for oneRoom in instructor_chatrooms:
            if oneRoom.course_id in theCourses:
                pass
            else:
                theCourses.append(oneRoom.course_id)
        ins_data['courses'] = theCourses
        ins_data['access_level'] = "Instructor"
        aRoom = instructor_chatrooms[0]
        ins_data['recent_room'] = getRecentRoom(aRoom)
        ins_data['recent_broadcast'] = Notice.objects.filter(chatroom_id=ins_data['recent_room']).order_by("-pk")
        try:
            notice = Notice.objects.filter(chatroom_id__instructor_username=ins_data['username']).order_by('time_stamp')[5]
        except IndexError:
            notice = None
        return render_to_response('instructor/instructor_home.html', ins_data, context)
    elif userType == 's':
        return redirect('/student')
    else:
        return redirect('/')

def getRecentRoom(aRoom):
    if aRoom == None:
        instructor_chatrooms = Chatroom.objects.all().filter(instructor_username=ins_data['username']).order_by("-pk")
        return instructor_chatrooms[0]
    else:
        return aRoom

def createChatroom(request):

    context = RequestContext(request)

    if request.method == 'POST':
        form = createChatroomForm(request.POST)

        if form.is_valid():
            new_data = form.save(commit = True)
            room_no = new_data.pk
            return redirect('/chat/'+str(room_no))
        else:
            print(form.errors)
    else:
        form = createChatroomForm()
