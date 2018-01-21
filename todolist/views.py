# from django.shortcuts import render

from django.http import HttpResponse
import datetime

def index(request):
    message = 'current time is: {}'.format(datetime.datetime.now())
    return HttpResponse(message)
