"""clginfo URL Configuration

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
from clginfoapp import views    #to use all the functions created of views.py program in clginfoapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name="homepage"),
    path('register/',views.SignUp,name="register"),  #url to register new user
    path('login/',views.login,name="login"), #url to login user
    path('logout/', views.logoutUser, name="logout"), #url to logout user
    path('topclgpage/',views.topclglist,name="topclgpage"), #url to display top colleges
    path('topcoursepage/',views.topcourse,name="topcoursepage"),    #url to display top courses
    path('topexamspage/',views.topexam,name="topexamspage"),    #url to display top exams
    path('clglistpage/',views.clglist,name="clglistpage"),  #url to display all the colleges in list
    path('clgsearch/',views.clgsearch,name="clgsearch"),    #url to search for the college as per the college name
    path('clgdetailspage/<int:pk>',views.clgdetailspage,name="clgdetailspage"), #url to view the details of a particular college
    path('coursedetailspage/<int:pk>',views.coursedetailspage,name="coursedetailspage"),    #url to view course description
    path('examsdetailspage/<int:pk>',views.examdetailspage,name="examdetailspage"), #url to view exam details
    path('chatbot',views.chatbotview,name="chatbot"), #url to chatbot
    path('admission/',views.admission,name="admission"),    #url to view admission page
]
