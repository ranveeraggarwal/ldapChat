from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from authenticator import ldapAuth

# Create your views here.


def authentication(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.REQUEST["username"]
        password = request.REQUEST["passwd"]
        authenticate = ldapAuth(request, username, password)
        if authenticate == 'VALID':
            userType = request.session.get('userType')
            if userType == 'f':
                return redirect('/instructor')
            else:
                return redirect('/student')
        else:
            return render_to_response('authentication/index.html', {'logged': False}, context)
    else:
        return redirect('authentication.views.index')


def index(request):
    context = RequestContext(request)
    username = request.session.get('username')
    if username is not None:
        userType = request.session.get('userType')
        if userType == 'f':
            return redirect('/instructor')
        else:
            return redirect('/student')
    return render_to_response('authentication/index.html', {'logged': 4}, context)

def logout(request):
    request.session.flush()
    return redirect("/")