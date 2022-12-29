
from django.contrib import admin
from django.urls import path, include
from chat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('auth/register', views.register)
    # path('auth/login', views.login)
]
