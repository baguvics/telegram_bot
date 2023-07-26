from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.MessageListView.as_view(), name='message-list'),
    path('commands/', views.CommandListView.as_view(), name='command-list'),
    path('message/<int:pk>/edit/', views.MessageUpdateView.as_view(), name='message-edit'),
    path('command/<int:pk>/edit/', views.CommandUpdateView.as_view(), name='command-edit'),

    path('message-api', views.MessageListCreate.as_view(), name='message-api'),
    path('command-api', views.CommandListCreate.as_view(), name='command-api'),
    # Добавьте остальные маршруты, если необходимо
]