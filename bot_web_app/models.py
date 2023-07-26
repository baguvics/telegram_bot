import django.db.models.deletion
from django.db import models


class Message(models.Model):
    user = models.ForeignKey('User', on_delete=django.db.models.deletion.SET_NULL, null=True)
    text = models.TextField(null=False)
    command = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.text}'


class User(models.Model):
    user = models.CharField(max_length=100)
    chat_id = models.CharField(max_length=100)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} - {self.chat_id}'


class BotCommand(models.Model):
    command = models.CharField(max_length=100)
    description = models.CharField(max_length=900, null=True, blank=True)

    def __str__(self):
        return f'{self.command}'
