
from django.contrib import admin
from django.urls import path, include
import chat 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('chat/', include('django.contrib.auth.urls'))
]
