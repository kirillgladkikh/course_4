from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Client  # , Mailing, Message, Log
from .forms import ClientForm  # , MailingForm, MessageForm

# class HomeView(TemplateView):
#     template_name = 'home_view.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['total_mailings'] = Mailing.objects.count()  # общее количество рассылок
#         context['active_mailings'] = Mailing.objects.filter(is_active=True).count()  # активные рассылки (предполагается поле is_active)
#         context['total_clients'] = Client.objects.count()  # количество уникальных получателей
#         return context


# Клиенты (Client)
class ClientListView(ListView):
    model = Client
    template_name = "clients_list.html"
    context_object_name = "clients"


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = "client_create.html"
    success_url = reverse_lazy("mailing:clients_list")

    def form_valid(self, form):
        messages.success(self.request, "Клиент создан!")
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = "client_update.html"
    success_url = reverse_lazy("mailing:clients_list")

    def form_valid(self, form):
        messages.success(self.request, "Клиент обновлён!")
        return super().form_valid(form)


class ClientDeleteView(DeleteView):
    model = Client
    template_name = "client_delete.html"
    success_url = reverse_lazy("mailing:clients_list")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Клиент удалён!")
        return super().delete(request, *args, **kwargs)


# Сообщения (Message)
class MessageListView(ListView):
    model = Message
    template_name = 'messages_list.html'
    context_object_name = 'messages'


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'message_create.html'
    success_url = reverse_lazy('mailing:messages_list')

    def form_valid(self, form):
        messages.success(self.request, 'Сообщение создано!')
        return super().form_valid(form)


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'message_update.html'
    success_url = reverse_lazy('mailing:messages_list')

    def form_valid(self, form):
        messages.success(self.request, 'Сообщение обновлено!')
        return super().form_valid(form)


class MessageDeleteView(DeleteView):
    model = Message
    template_name = "message_delete.html"
    success_url = reverse_lazy('mailing:messages_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Сообщение удалено!')
        return super().delete(request, *args, **kwargs)


# # Рассылки (Mailing)
# class MailingListView(ListView):
#     model = Mailing
#     template_name = 'mailings_list.html'
#     context_object_name = 'mailings'
#
#
# class MailingCreateView(CreateView):
#     model = Mailing
#     form_class = MailingForm
#     template_name = 'mailing_form.html'-------------
#     success_url = reverse_lazy('mailing:mailing_list')--------------
#
#     def form_valid(self, form):
#         messages.success(self.request, 'Рассылка создана!')
#         return super().form_valid(form)
#
#
# class MailingUpdateView(UpdateView):
#     model = Mailing
#     form_class = MailingForm
#     template_name = 'mailing_form.html'-------------
#     success_url = reverse_lazy('mailing:mailing_list')--------------
#
#     def form_valid(self, form):
#         messages.success(self.request, 'Рассылка обновлена!')
#         return super().form_valid(form)
#
#
# class MailingDeleteView(DeleteView):
#     model = Mailing
#     template_name = "mailing_delete.html"---------------
#     success_url = reverse_lazy('mailing:mailings_list')--------------
#
#     def delete(self, request, *args, **kwargs):
#         messages.success(request, 'Рассылка удалена!')
#         return super().delete(request, *args, **kwargs)
