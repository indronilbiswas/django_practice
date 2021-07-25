"""LearnDjangoOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from LearnDjangoOnline import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('contact/', views.contact, name="contact"),
    path('enquiry/', views.enquiry, name="enquiry"),
    path('table/', views.table, name="table"),
    path('add_get/', views.addition_get, name="add_get"),
    path('add_post/', views.addition_post, name="add_post"),
    path('displayname/', views.display_name, name="displayname"),
    path('welcome/', views.welcome, name="welcome"),
    path('welcomeaction/', views.welcome_action, name="welcomeaction"),
    path('djangoform/', views.django_form, name="djangoform"),
    path('calculator/', views.calculator, name="calculator"),
    path('evenodd/', views.evenodd, name="evenodd"),
    path('marksheet/', views.marksheet, name="marksheet"),
    path('newsdetails/<slug>', views.newsdetails),
    path('blog/', views.blog),
    path('course/<cid>', views.course),

]
