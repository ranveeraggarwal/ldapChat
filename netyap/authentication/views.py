from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from authenticator import authenticate
import forms

# Create your views here.


def authentication(request):
    context = RequestContext(request)
    form = forms.AuthenticationForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        remember = form.cleaned_data['remember']

        if remember:
            '''
            Year long Session
            '''
            request.session.set_expiry(31536000)
        else:
            request.session.set_expiry(0)

        auth = authenticate(request, username, password)
        if auth == 'VALID':
            user_type = request.session.get('userType')
            if user_type == 'f':
                return redirect('/instructor')
            else:
                return redirect('/student')
        form.add_error(None, 'Invalid Username/Password')
    return render_to_response('authentication/index.html', {'form': form}, context)


def index(request):
    context = RequestContext(request)
    username = request.session.get('username')
    if username is not None:
        userType = request.session.get('userType')
        if userType == 'f':
            return redirect('/instructor')
        else:
            return redirect('/student')
    form = forms.AuthenticationForm()
    return render_to_response('authentication/index.html', {'logged': 4, 'form': form}, context)


def logout(request):
    request.session.flush()
    return redirect("/")