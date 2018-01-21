from django.conf.urls import url
from django.contrib import admin
from views import todo_list, complete, delete


urlpatterns = [
    url(r'^admin/', admin.site.urls), # administration
    # url(r'^$', views.index, name='index'),
    url(r'^$', todo_list), # main page
    url(r'^delete/(?P<pk>\d+)/', delete), # delete a todo-item
    url(r'^complete/(?P<pk>\d+)/', complete), # complete a todo-item
]
