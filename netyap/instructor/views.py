from django.shortcuts import render
from django.template import RequestContext

# Create your views here.

def index(request):
    session = request.session
    context = RequestContext(request)
    type = request.session.get('type')
    ins_data = {}
    if type == 'f':
        ins_data['name'] = session.get('name')


    return render('/instructor/instructor_home.html', {'instructor_name': 'varsha'})