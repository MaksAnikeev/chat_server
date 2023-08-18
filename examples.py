import requests
from datetime import datetime
from pprint import pprint

'''Создаем юзера'''
url = 'http://127.0.0.1:9000/user/add'
payload = {
    'username': 'Krashiks',
    'created_at': datetime.now()
}
response = requests.post(url, data=payload)
response.raise_for_status()
print(response.json())


'''Создаем чат'''
url = 'http://127.0.0.1:9000/chat/add'
payload = {
    'name': 'Workerik',
    'users': [12, 15, 17],
    'created_at': datetime.now()
}
response = requests.post(url, data=payload)
response.raise_for_status()
print(response.json())


'''Создаем сообщение'''
url = 'http://127.0.0.1:9000/message/add'
payload = {
    'chat': 7,
    'author': 17,
    'created_at': datetime.now(),
    'text': 'вперед'
}
response = requests.post(url, data=payload)
response.raise_for_status()
print(response.json())


'''Получаем все чаты юзера'''
url = 'http://127.0.0.1:9000/chats/get'
payload = {
    'user_id': 17,
}
response = requests.post(url, data=payload)
response.raise_for_status()
print(response.json())


'''Получаем все сообщения чата'''
url = 'http://127.0.0.1:9000/messages/get'
payload = {
    'chat_id': 7,
}
response = requests.post(url, data=payload)
response.raise_for_status()
pprint(response.json())
