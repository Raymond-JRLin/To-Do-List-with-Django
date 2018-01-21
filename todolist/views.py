from django.shortcuts import render
from models import Todo

### testing without database
# class Todo:
#     def __init__(self, description, isCompleted):
#         self.description = description
#         self.isCompleted = isCompleted
###


def todo_list(request):
    # because we use the same form/page to show and add, we need to determine which request we got
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            title = request.POST.get('title')
            # create a new todo
            Todo.objects.create(title=title)

    list = Todo.objects.all() # get the todolists in database including what we added above

    return render(request, 'todolist.html', locals())






###
# from django.http import HttpResponse
# import datetime
#
# def index(request):
#     message = 'current time is: {}'.format(datetime.datetime.now())
#     return HttpResponse(message)
###
