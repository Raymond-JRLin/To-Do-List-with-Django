from django.conf.urls import url
from django.contrib import admin
from todolist import views


urlpatterns = [
    url(r'^admin/', admin.site.urls), # administration
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.todolist), # main page
    # url(r'^delete/(?P<pk>\d+)/', views.delete), # delete a todo-item
    # url(r'^complete/(?P<pk>\d+)/', views.complete), # complete a todo-item
]
