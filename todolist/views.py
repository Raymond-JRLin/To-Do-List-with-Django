from django.shortcuts import render
from models import Todo

### testing without database
# class Todo:
#     def __init__(self, description, isCompleted):
#         self.description = description
#         self.isCompleted = isCompleted
###


def todo_list(request):
    list = Todo.objects.all()

    return render(request, 'todolist.html', locals())






###
# from django.http import HttpResponse
# import datetime
#
# def index(request):
#     message = 'current time is: {}'.format(datetime.datetime.now())
#     return HttpResponse(message)
###
