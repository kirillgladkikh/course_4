from django import forms
from .models import Client, Message  # , Mailing


# Клиенты (Client)
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["email", "full_name", "comment", "owner"]
        labels = {
            "email": "Контактный email",
            "full_name": "ФИО",
            "comment": "Комментарий",
            "owner": "Владелец (User)",
        }
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "example@domain.com"}),
            "full_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Фамилия Имя Отчество",
                    "maxlength": "100",  # явно указываем лимит из модели
                }
            ),
            "comment": forms.TextInput(
                attrs={  # CharField → TextInput
                    "class": "form-control",
                    "maxlength": "255",
                    "placeholder": "Кратко о клиенте...",
                }
            ),
            "owner": forms.Select(attrs={"class": "form-select"}),  # для ForeignKey лучше form-select
        }


# Сообщения (Message)
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'body', 'owner']
        labels = {
            "subject": "Тема письма",
            "body": "Тело письма",
            "owner": "Владелец (User)",
        }
        widgets = {
            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Тема письма",
                    "maxlength": "200",  # явно указываем лимит из модели
                }
            ),
            'body': forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Тело письма",
                    'rows': 10,
                }
            ),
            "owner": forms.Select(attrs={"class": "form-select"}),  # для ForeignKey лучше form-select
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

