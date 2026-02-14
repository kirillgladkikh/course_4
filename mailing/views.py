from django.views.generic import TemplateView, View, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Client, Message, Mailing, Log
from .forms import ClientForm, MessageForm, MailingForm
from django.shortcuts import render, get_object_or_404, redirect


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
    template_name = "messages_list.html"
    context_object_name = "messages"


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = "message_create.html"
    success_url = reverse_lazy("mailing:messages_list")

    def form_valid(self, form):
        messages.success(self.request, "Сообщение создано!")
        return super().form_valid(form)


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = "message_update.html"
    success_url = reverse_lazy("mailing:messages_list")

    def form_valid(self, form):
        messages.success(self.request, "Сообщение обновлено!")
        return super().form_valid(form)


class MessageDeleteView(DeleteView):
    model = Message
    template_name = "message_delete.html"
    success_url = reverse_lazy("mailing:messages_list")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Сообщение удалено!")
        return super().delete(request, *args, **kwargs)


# Рассылки (Mailing)
class MailingListView(ListView):
    model = Mailing
    template_name = "mailings_list.html"
    context_object_name = "mailings"


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = "mailing_form.html"
    success_url = reverse_lazy("mailing:mailings_list")

    def form_valid(self, form):
        messages.success(self.request, "Рассылка создана!")
        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = "mailing_form.html"
    success_url = reverse_lazy("mailing:mailings_list")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.update_status()  # ← пересчёт статуса при открытии
        return obj

    def form_valid(self, form):
        messages.success(self.request, "Рассылка обновлена!")
        return super().form_valid(form)


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = "mailing_delete.html"
    success_url = reverse_lazy("mailing:mailings_list")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Рассылка удалена!")
        return super().delete(request, *args, **kwargs)


# Попытки рассылки
class MailingSendListView(ListView):
    model = Mailing
    template_name = "mailing_send_list.html"  # ← обратите внимание на имя шаблона!
    context_object_name = "mailings"

    def get_queryset(self):
        qs = super().get_queryset()
        for mailing in qs:
            mailing.update_status()
        return qs


class SendMailingView(View):
    def get(self, request, pk):
        # Получаем конкретную рассылку для подтверждения
        mailing = get_object_or_404(Mailing, pk=pk)
        mailing.update_status()  # обновляем статус перед показом
        return render(request, "mailing_send.html", {"mailing": mailing})

    def post(self, request, pk):
        mailing = get_object_or_404(Mailing, pk=pk)
        try:
            mailing.send_mailing()
            mailing.status = "running"
            mailing.save()
            messages.success(request, "Рассылка запущена!")
            return redirect("mailing:mailing_send_list")  # возвращаемся к списку
        except Exception as e:
            messages.error(request, f"Ошибка при отправке: {str(e)}")
            return render(request, "mailing_send.html", {"mailing": mailing, "error": str(e)})


# Попытки рассылки (Log)
class LogListView(ListView):
    model = Log
    template_name = "mailing_log.html"
    context_object_name = "logs"
    ordering = ["-attempt_time"]  # сортировка по времени (новые сверху)

    def get_queryset(self):
        return Log.objects.select_related("mailing", "client").order_by("-attempt_time")


# Главная страница
class HomeView(TemplateView):
    template_name = 'home_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()  # Получаем текущую дату и время

        # 1. Общее количество всех созданных рассылок
        context['total_mailings'] = Mailing.objects.count()

        # 2. Количество активных рассылок
        # Активная рассылка: статус = 'Запущена' И текущее время в интервале [start_time, end_time]
        active_mailings = Mailing.objects.filter(
            status=Mailing.STATUS_RUNNING,  # статус "Запущена"
            start_time__lte=now,           # текущее время ≥ start_time
            end_time__gte=now              # текущее время ≤ end_time
        ).count()
        context['active_mailings'] = active_mailings

        # 3. Количество уникальных получателей (клиентов)
        context['total_clients'] = Client.objects.count()

        return context
