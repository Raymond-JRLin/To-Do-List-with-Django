from django.conf.urls import include, url
from django.contrib import admin

from views import get_time

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', get_time),
    url(r'', include('todolist.urls'))
]
