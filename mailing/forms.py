from django import forms
from .models import Client, Mailing, Message

# Клиенты (Client)
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['email', 'full_name', 'comment', 'owner']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
        }

# # Рассылки (Mailing)
# class MailingForm(forms.ModelForm):
#     class Meta:
#         model = Mailing
#         fields = ['start_datetime', 'end_datetime', 'period', 'status', 'message', 'clients', 'owner']
#         widgets = {
#             'start_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#             'end_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#         }
#
# # Сообщения (Message)
# class MessageForm(forms.ModelForm):
#     class Meta:
#         model = Message
#         fields = ['subject', 'body', 'owner']
#         widgets = {
#             'body': forms.Textarea(attrs={'rows': 10}),
#         }
