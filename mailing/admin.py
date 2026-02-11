from django.contrib import admin
from .models import Client, Mailing, Message, Log

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'owner']
    list_filter = ['owner']
    search_fields = ['full_name', 'email']

# @admin.register(Mailing)
# class MailingAdmin(admin.ModelAdmin):
#     list_display = ['id', 'start_datetime', 'status', 'owner']
#     list_filter = ['status', 'owner']
#     date_hierarchy = 'start_datetime'
#
# @admin.register(Message)
# class MessageAdmin(admin.ModelAdmin):
#     list_display = ['subject', 'owner']
#     list_filter = ['owner']
#
# @admin.register(Log)
# class LogAdmin(admin.ModelAdmin):
#     list_display = ['datetime', 'status', 'mailing']
#     list_filter = ['status', 'datetime']
#     date_hierarchy = 'datetime'
