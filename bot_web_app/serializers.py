from rest_framework import serializers
from .models import Message, BotCommand


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'user', 'text', 'command', 'date')


class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotCommand
        fields = ('id', 'command', 'description')
