from django.template import RequestContext
from django.shortcuts import render, render_to_response

def index(request):
    context = RequestContext(request)

    context_dict = {'boldMessage': "I am bold font from the context"}

    return render_to_response('sample-app/index.html', context_dict, context)