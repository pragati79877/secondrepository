from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def timeinfo(r):
        date = datetime.datetime.now()
        msg='<h1>Hello Goodevening</h1>'
        msg = msg+'Your System Time is: '+str(date)
        return HttpResponse(msg)