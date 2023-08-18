from django.urls import path

from .views import add_user, add_chat, add_message, get_messages, get_chats

app_name = "app"

urlpatterns = [
    path('user/add', add_user),
    path('chat/add', add_chat),
    path('message/add', add_message),
    path('chats/get', get_chats),
    path('messages/get', get_messages)
]
