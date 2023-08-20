from django.contrib import admin
from .models import User, Chat, Message


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'author')
