from django.urls import path
from django.views.generic import TemplateView
from mailing.views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView
from mailing.apps import MailingConfig


app_name = MailingConfig.name

urlpatterns = [
    path('', TemplateView.as_view(template_name='home_view.html'), name='home_view'),

    # Клиенты
    path('clients/', ClientListView.as_view(), name='clients_list'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('clients/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),

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
