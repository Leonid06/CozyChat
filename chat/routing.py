from django.urls import path, include 
from chat.consumers import ChatConsumer 

websocket_urlpatterns = [
    path("ws/socket-server", ChatConsumer.as_asgi())
]