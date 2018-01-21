from django.shortcuts import render


class Todo:
    def __init__(self, description, isCompleted):
        self.description = description
        self.isCompleted = isCompleted


def todo_list(request):
    list = []

    for value in range(0, 10):
        list.append(Todo("item" + str(value), False))

    return render(request, 'todolist.html', locals())






###
# from django.http import HttpResponse
# import datetime
#
# def index(request):
#     message = 'current time is: {}'.format(datetime.datetime.now())
#     return HttpResponse(message)
###
