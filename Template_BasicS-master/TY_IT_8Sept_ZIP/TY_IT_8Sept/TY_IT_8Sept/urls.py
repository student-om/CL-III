"""TY_IT_8Sept URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from student.views import view_hello,view_record,view_hello_20

# from student.views import view_django


from django.conf.urls import url



#   https://django-tables2.readthedocs.io/en/latest/pages/tutorial.html    REPORTS GEN

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^hello1/', view_hello),
    url(r'^hello20/', view_hello_20),
    url(r'^record1/', view_record),
    # url(r'^django/', view_django),




]
