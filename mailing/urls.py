from django.urls import path
from django.views.decorators.cache import cache_page
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
    # Клиенты
    path("clients/", cache_page(60 * 15)(ClientListView.as_view()), name="clients_list"),
    path("clients/create/", cache_page(60 * 15)(ClientCreateView.as_view()), name="client_create"),
    path("clients/update/<int:pk>/", cache_page(60 * 15)(ClientUpdateView.as_view()), name="client_update"),
    path("clients/delete/<int:pk>/", cache_page(60 * 15)(ClientDeleteView.as_view()), name="client_delete"),
    # Сообщения
    path("messages/", cache_page(60 * 15)(MessageListView.as_view()), name="messages_list"),
    path("messages/create/", cache_page(60 * 15)(MessageCreateView.as_view()), name="message_create"),
    path("messages/update/<int:pk>/", cache_page(60 * 15)(MessageUpdateView.as_view()), name="message_update"),
    path("messages/delete/<int:pk>/", cache_page(60 * 15)(MessageDeleteView.as_view()), name="message_delete"),
    # Рассылки
    path("mailings/", cache_page(60 * 15)(MailingListView.as_view()), name="mailings_list"),
    path("mailings/create/", cache_page(60 * 15)(MailingCreateView.as_view()), name="mailing_create"),
    path("mailings/update/<int:pk>/", cache_page(60 * 15)(MailingUpdateView.as_view()), name="mailing_update"),
    path("mailings/delete/<int:pk>/", cache_page(60 * 15)(MailingDeleteView.as_view()), name="mailing_delete"),
    # Рассылки - ОТПРАВКА
    path("mailings/send/", cache_page(60 * 15)(MailingSendListView.as_view()), name="mailing_send_list"),
    path("mailings/send/<int:pk>/", cache_page(60 * 15)(SendMailingView.as_view()), name="mailing_send"),
    # Рассылки - ЛОГ
    path("logs/", cache_page(60 * 15)(LogListView.as_view()), name="mailing_log"),
]
