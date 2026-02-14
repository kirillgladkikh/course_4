from django.urls import path
from django.views.generic import TemplateView
from mailing.views import (
    HomeView,
    ClientListView,
    ClientCreateView,
    ClientUpdateView,
    ClientDeleteView,
    MessageListView,
    MessageCreateView,
    MessageUpdateView,
    MessageDeleteView,
    MailingListView,
    MailingCreateView,
    MailingUpdateView,
    MailingDeleteView,
    MailingSendListView,
    SendMailingView,
    LogListView,
)
from mailing.apps import MailingConfig

app_name = MailingConfig.name

urlpatterns = [
    # Главная страница
    path("", HomeView.as_view(), name="home_view"),
    # path("", TemplateView.as_view(template_name="home_view.html"), name="home_view"),
    # Клиенты
    path("clients/", ClientListView.as_view(), name="clients_list"),
    path("clients/create/", ClientCreateView.as_view(), name="client_create"),
    path("clients/update/<int:pk>/", ClientUpdateView.as_view(), name="client_update"),
    path("clients/delete/<int:pk>/", ClientDeleteView.as_view(), name="client_delete"),
    # Сообщения
    path("messages/", MessageListView.as_view(), name="messages_list"),
    path("messages/create/", MessageCreateView.as_view(), name="message_create"),
    path("messages/update/<int:pk>/", MessageUpdateView.as_view(), name="message_update"),
    path("messages/delete/<int:pk>/", MessageDeleteView.as_view(), name="message_delete"),
    # Рассылки
    path("mailings/", MailingListView.as_view(), name="mailings_list"),
    path("mailings/create/", MailingCreateView.as_view(), name="mailing_create"),
    path("mailings/update/<int:pk>/", MailingUpdateView.as_view(), name="mailing_update"),
    path("mailings/delete/<int:pk>/", MailingDeleteView.as_view(), name="mailing_delete"),
    # Рассылки - ОТПРАВКА
    path("mailings/send/", MailingSendListView.as_view(), name="mailing_send_list"),
    path("mailings/send/<int:pk>/", SendMailingView.as_view(), name="mailing_send"),
    # Рассылки - ЛОГ
    path("logs/", LogListView.as_view(), name="mailing_log"),
]
