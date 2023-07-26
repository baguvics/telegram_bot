from django.contrib import admin
from .models import Message, User, BotCommand


admin.site.register(Message)
admin.site.register(User)
admin.site.register(BotCommand)
