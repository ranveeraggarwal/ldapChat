__author__ = 'kabraadit'

from django.db import connection
from time import time
from operator import add
import re
from django.shortcuts import redirect

class StatsMiddleware(object):

    def process_request(self,request):
        session = request.session
        path = request.get_full_path()
        print path
        if path != '/' and session.get('username')==None:
            return redirect('/')


