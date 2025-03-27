from django.contrib import admin
from django.urls import include, re_path

from django.urls import include, re_path

from student.views import view_hello,view_record,view_hello_20
#from django.conf.urls import url

#from django.urls import include, re_path
#from myapp.views import home


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^hello1/', view_hello, name='home'),
    re_path(r'^hello20/', view_hello_20),
    re_path(r'^record1/', view_record),
    #re_path(r'^$', home, name='home'),
    #url(r'^hello1/', view_hello),
    #url(r'^hello20/', view_hello_20),
    #url(r'^record1/', view_record),
]



