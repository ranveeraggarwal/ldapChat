from django.shortcuts import render, render_to_response

# Create your views here.

def authentication(request):
    if request.method == 'POST':
        username = request.REQUEST["username"]
        password = request.REQUEST["passwd"]
        print username, password

def index(request):
    return render_to_response('authentication/index.html', {})