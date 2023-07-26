from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, FormView
from .models import Message, BotCommand
from rest_framework import generics
from .serializers import MessageSerializer, CommandSerializer
from .forms import MessageForm, CommandForm
from django.core import serializers


class MessageListView(ListView):
    model = Message
    template_name = 'message_list.html'
    context_object_name = 'messages'
    ordering = ['-date']


class MessageUpdateView(FormView):
    template_name = 'message_edit.html'
    form_class = MessageForm

    def form_valid(self, form):
        message_id = self.kwargs['pk']
        message = Message.objects.get(pk=message_id)
        message.text = form.cleaned_data['text']
        message.command = form.cleaned_data['command']
        message.save()
        return redirect('message-list')


class CommandListView(ListView):
    model = BotCommand
    template_name = 'command_list.html'
    context_object_name = 'commands'


class CommandUpdateView(FormView):
    template_name = 'command_edit.html'
    form_class = CommandForm

    def form_valid(self, form):
        command_id = self.kwargs['pk']
        command = BotCommand.objects.get(pk=command_id)
        command.command = form.cleaned_data['command']
        command.description = form.cleaned_data['description']
        command.save()
        return redirect('command-list')


class MessageListCreate(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class CommandListCreate(generics.ListCreateAPIView):
    queryset = BotCommand.objects.all()
    serializer_class = CommandSerializer
