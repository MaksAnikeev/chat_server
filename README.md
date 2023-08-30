# Тестовое задание для стажера. 

Цель задания – разработать чат-сервер, предоставляющий HTTP API для работы с чатами и сообщениями пользователя.

Детали реализации:
Сервер должен быть доступен на порту 9000

Основные API методы:

1. Добавить нового пользователя
- Ответ: id созданного пользователя или HTTP-код ошибки + описание ошибки.

2. Создать новый чат между пользователями
- Ответ: id созданного чата или HTTP-код ошибки или HTTP-код ошибки + описание ошибки.
Количество пользователей в чате не ограничено.

3. Отправить сообщение в чат от лица пользователя
- Ответ: id созданного сообщения или HTTP-код ошибки + описание ошибки.

4. Получить список чатов конкретного пользователя
- Ответ: cписок всех чатов со всеми полями, отсортированный по времени создания последнего сообщения в чате (от позднего к раннему). Или HTTP-код ошибки + описание ошибки.

5. Получить список сообщений в конкретном чате
- Ответ: список всех сообщений чата со всеми полями, отсортированный по времени создания сообщения (от раннего к позднему). Или HTTP-код ошибки + описание ошибки.

## Запуск:

Скачайте код:
```
git clone https://github.com/MaksAnikeev/chat_server
```

Перейдите в каталог проекта:
```
cd chat_server
```

[Установите Python](https://www.python.org/), если этого ещё не сделали.

Проверьте, что `python` установлен и корректно настроен. Запустите его в командной строке:
```
python --version
```
**Важно!** Версия Python должна быть не ниже 3.6.

Возможно, вместо команды `python` здесь и в остальных инструкциях этого README придётся использовать `python3`. Зависит это от операционной системы и от того, установлен ли у вас Python старой второй версии.

В каталоге проекта создайте виртуальное окружение:
```
python -m venv venv
```
Активируйте его. На разных операционных системах это делается разными командами:

- Windows: `.\venv\Scripts\activate`
- MacOS/Linux: `source venv/bin/activate`


Установите зависимости в виртуальное окружение:
```
pip install -r requirements.txt
```

Определите переменную окружения `SECRET_KEY`. Создать файл `.env` в каталоге `short_links/` и положите туда такой код:
```
SECRET_KEY=django-.......
```

Если вы запускаете проект не на локальном компьютере, а на арендованном сервере,
то необходимо прописать в файле `.env` ip сервера
```
ALLOWED_HOSTS=80.249....
```

Если вы закончили с отладкой и переходите в "боевой" режим, то укажите
в файле `.env`:
```
DEBUG=False
```

Отмигрируйте базу данных на своем компьютере функцией:

```
python manage.py migrate
```

Запустите сервер на порту 9000:

```
python manage.py runserver 9000
```

Для выполнения запросов и создания базы данных с пользователями и чатами необходимо использовать файл
```
example.py
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
