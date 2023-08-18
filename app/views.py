from .serializers import UserSerializer, ChatSerializer, MessageSerializer
from .models import User, Chat, Message
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist


@api_view(['POST'])
def add_user(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        User.objects.get(username=serializer.validated_data['username'])
        response = {'info': 'Пользователь с таким именем уже существует'}
        return Response(response, status=200)

    except ObjectDoesNotExist:
        user = User.objects.create(
            username=serializer.validated_data['username'],
            created_at=serializer.validated_data['created_at']
        )

        serializer = UserSerializer(user)
        return Response(serializer.data, status=200)


@api_view(['POST'])
def add_chat(request):
    serializer = ChatSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        Chat.objects.get(name=serializer.validated_data['name'])
        response = {'info': 'Чат с таким именем уже существует'}
        return Response(response, status=200)

    except ObjectDoesNotExist:
        chat = Chat.objects.create(
            name=serializer.validated_data['name'],
            created_at=serializer.validated_data['created_at']
        )
        chat.users.set(serializer.validated_data['users'])

        serializer = ChatSerializer(chat)
        return Response(serializer.data, status=200)


@csrf_exempt
@api_view(['POST'])
def add_message(request):
    serializer = MessageSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    message = Message.objects.create(
        chat=serializer.validated_data['chat'],
        author=serializer.validated_data['author'],
        created_at=serializer.validated_data['created_at'],
        text=serializer.validated_data['text']
    )
    serializer = MessageSerializer(message)
    return Response(serializer.data, status=200)


@csrf_exempt
def get_chats(request):
    user = User.objects.get(id=request.POST.get('user_id'))
    chats = [chat.name for chat in user.chats.all()]
    response = {'chats': chats}
    return JsonResponse(response, status=200)


@csrf_exempt
def get_messages(request):
    chat = Chat.objects.get(id=request.POST.get('chat_id'))
    messages = [MessageSerializer(message).data for message in chat.messages.all().order_by('created_at')]
    response = {'messages': messages}
    return JsonResponse(response, status=200)
