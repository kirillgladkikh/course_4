from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings


# Модель "Клиент (USERS)"
class Client(models.Model):
    email = models.EmailField(verbose_name="Контактный email")
    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    comment = models.CharField(max_length=255, verbose_name="Комментарий", blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец", related_name="clients")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


# Модель "Сообщение (письмо)"
class Message(models.Model):
    subject = models.CharField(max_length=200, verbose_name="Тема письма")
    body = models.TextField(verbose_name="Тело письма")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец", related_name="messages")

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


# Модель "Попытки рассылки (Логи)"
class Log(models.Model):
    SUCCESS = "Успешно"
    ERROR = "Ошибка"
    STATUS_CHOICES = [
        (SUCCESS, SUCCESS),
        (ERROR, ERROR),
    ]

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='logs')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    attempt_time = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время попытки")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        verbose_name="Статус"
    )
    server_response = models.TextField(blank=True, null=True, verbose_name="Ответ почтового сервера")

    def __str__(self):
        return f"Лог {self.id}: {self.status} для {self.client.full_name}"

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылок"


# Модель "Рассылка"
class Mailing(models.Model):
    # Статус рассылки (вычисляется динамически)
    STATUS_CREATED = "Создана"
    STATUS_RUNNING = "Запущена"
    STATUS_COMPLETED = "Завершена"

    STATUS_CHOICES = [
        (STATUS_CREATED, STATUS_CREATED),
        (STATUS_RUNNING, STATUS_RUNNING),
        (STATUS_COMPLETED, STATUS_COMPLETED),
    ]

    start_time = models.DateTimeField(verbose_name="Дата и время начала отправки")
    end_time = models.DateTimeField(verbose_name="Дата и время окончания отправки")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CREATED, verbose_name="Статус")
    message = models.ForeignKey("Message", on_delete=models.CASCADE, verbose_name="Сообщение")
    clients = models.ManyToManyField("Client", verbose_name="Получатели")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец", related_name="mailings")

    def __str__(self):
        return f"Рассылка {self.id}: {self.status}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"

    def update_status(self):
        """Вычисляет и обновляет статус рассылки на основе текущего времени."""
        now = timezone.now()

        if now < self.start_time:
            new_status = self.STATUS_CREATED
        elif self.start_time <= now <= self.end_time:
            new_status = self.STATUS_RUNNING
        else:
            new_status = self.STATUS_COMPLETED

        # Если статус изменился — сохраняем в БД
        if self.status != new_status:
            self.status = new_status
            self.save(update_fields=["status"])

    def send_mailing(self):
        now = timezone.now()

        # Проверка: текущее время в интервале [start_time, end_time]?
        if not (self.start_time <= now <= self.end_time):
            raise ValueError(
                f"Рассылка не может быть отправлена. Текущее время {now} не входит в интервал "
                f"[{self.start_time}, {self.end_time}]."
            )

        # Перебираем всех получателей
        for client in self.clients.all():
            try:
                # Отправка письма
                send_mail(
                    subject=self.message.subject,
                    message=self.message.body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email],
                    fail_silently=False,
                )
                # Запись успешной попытки
                Log.objects.create(
                    mailing=self,
                    client=client,
                    status='Успешно',
                    server_response=''
                )
            except Exception as e:
                # Запись неудачной попытки с текстом ошибки
                Log.objects.create(
                    mailing=self,
                    client=client,
                    status='Не успешно',
                    server_response=str(e)
                )

        # Обновляем статус рассылки
        self.status = self.STATUS_RUNNING
        self.save(update_fields=['status'])



# # Модель "Логи (Попытки рассылки)"
# class Log(models.Model):
#     SUCCESS = "Успешно"
#     ERROR = "Ошибка"
#     STATUS_CHOICES = [
#         (SUCCESS, "Успешно"),
#         (ERROR, "Ошибка"),
#     ]
#
#     datetime = models.DateTimeField(verbose_name="Дата и время")
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name="Статус")
#     server_response = models.TextField(blank=True, null=True, verbose_name="Ответ сервера")
#     mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name="Рассылка")
#
#     def __str__(self):
#         return f"Логи рассылки {self.mailing.id}: {self.status}"
#
#     class Meta:
#         verbose_name = "Логи рассылки"
#         verbose_name_plural = "Логи рассылок"
