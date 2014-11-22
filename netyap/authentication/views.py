from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
import json
from authenticator import ldapAuth

# Create your views here.

def authentication(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.REQUEST["username"]
        password = request.REQUEST["passwd"]
        print username, password
        authenticate = ldapAuth(username, password)
        if authenticate == 'VALID':
            return render_to_response('authentication/index.html', {'logged': True}, context)
        else:
            return render_to_response('authentication/index.html', {'logged': False}, context)
    else:
        return render_to_response('authentication/index.html', {'logged': 3}, context)

def index(request):
    return render_to_response('authentication/index.html', {'logged': 4}, context_instance=RequestContext(request))