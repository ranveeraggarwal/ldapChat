from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.

def index(request):
    session = request.session
    context = RequestContext(request)
    type = request.session.get('type')
    ins_data = {}
    if type == 'f':
        ins_data['name'] = session.get('name')
        ins_data['username'] = session.get('username')

    return render_to_response('instructor/instructor_home.html', {'instructor_name': 'varsha'}, context)