from django.contrib import admin
from .models import Client, Message, Mailing  # , Log


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "owner"]
    list_filter = ["owner"]
    search_fields = ["full_name", "email"]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["subject", "owner"]
    list_filter = ["owner"]


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ["id", "start_time", "status", "owner"]
    list_filter = ["status", "owner"]
    date_hierarchy = "start_time"


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ["mailing", "client", "attempt_time", "status"]
    list_filter = ["status", "attempt_time", "mailing"]
    search_fields = ["client__full_name", "mailing__id"]
    date_hierarchy = "attempt_time"
    readonly_fields = ["attempt_time", "server_response"]

    def has_add_permission(self, request):
        return False  # Логи создаются автоматически — ручное добавление не нужно
