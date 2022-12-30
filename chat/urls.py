from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('login_user', views.login_user, name = 'login'),
   path('register_user', views.register, name = 'register'),
   path('main', views.main, name = 'main')
]