from django.urls import path
from . import views
from mailing.apps import MailingConfig


app_name = MailingConfig.name

urlpatterns = [
    # Клиенты
    path('clients/', views.ClientListView.as_view(), name='client_list'),
    path('clients/create/', views.ClientCreateView.as_view(), name='client_create'),
    path('clients/update/<int:pk>/', views.ClientUpdateView.as_view(), name='client_update'),
    path('clients/delete/<int:pk>/', views.ClientDeleteView.as_view(), name='client_delete'),

    # # Рассылки
    # path('mailings/', views.MailingListView.as_view(), name='mailing_list'),
    # path('mailings/create/', views.MailingCreateView.as_view(), name='mailing_create'),
    # path('mailings/update/<int:pk>/', views.MailingUpdateView.as_view(), name='mailing_update'),
    # path('mailings/delete/<int:pk>/', views.MailingDeleteView.as_view(), name='mailing_delete'),
    #
    # # Сообщения
    # path('messages/', views.MessageListView.as_view(), name='message_list'),
    # path('messages/create/', views.MessageCreateView.as_view(), name='message_create'),
    # path('messages/update/<int:pk>/', views.MessageUpdateView.as_view(), name='message_update'),  # обновление сообщения
    # path('messages/delete/<int:pk>/', views.MessageDeleteView.as_view(), name='message_delete'),  # удаление сообщения
]
