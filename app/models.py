from django.db import models


class User(models.Model):
    username = models.CharField(
        max_length=50,
        verbose_name='имя пользователя',
    )
    created_at = models.DateTimeField(
        verbose_name='время создания'
    )

    def __str__(self):
        return self.username


class Chat(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='название чата',
    )

    created_at = models.DateTimeField(
        verbose_name='время создания'
    )

    users = models.ManyToManyField(
        User,
        related_name='chats'
    )

    def __str__(self):
        return self.name


class Message(models.Model):
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name='чат'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='messages',
        verbose_name='автор',
        null=True
    )

    text = models.TextField(
        verbose_name='текст сообщения'
    )

    created_at = models.DateTimeField(
        verbose_name='время создания'
    )

    def __str__(self):
        return self.author.username
