"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha', include('captcha.urls')),
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.register),
    path('generaluserlist/', views.generaluserlist),
    path('adminuserlist/', views.adminuserlist),
    path('adduser/', views.adduser),
    path('deleteuser/', views.deleteuser),
    path('updateuser/', views.updateuser),
    path('generalstudentlist/', views.generalstudentlist),
    path('generalgradelist/', views.generalgradelist),
    path('adminstudentlist/', views.adminstudentlist),
    path('addstudent/', views.addstudent),
    path('deletestudent/', views.deletestudent),
    path('updatestudent/', views.updatestudent),
    path('admingradelist/', views.admingradelist),
    path('addgrade/', views.addgrade),
    path('deletegrade/', views.deletegrade),
    path('updategrade/', views.updategrade)
]
