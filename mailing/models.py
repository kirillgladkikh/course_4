from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


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


# Модель "Рассылка"
class Mailing(models.Model):
    # Статус рассылки (вычисляется динамически)
    STATUS_CREATED = 'Создана'
    STATUS_RUNNING = 'Запущена'
    STATUS_COMPLETED = 'Завершена'

    STATUS_CHOICES = [
        (STATUS_CREATED, STATUS_CREATED),
        (STATUS_RUNNING, STATUS_RUNNING),
        (STATUS_COMPLETED, STATUS_COMPLETED),
    ]

    start_time = models.DateTimeField(verbose_name="Дата и время начала отправки")
    end_time = models.DateTimeField(verbose_name="Дата и время окончания отправки")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_CREATED,
        verbose_name="Статус"
    )
    message = models.ForeignKey(
        'Message',
        on_delete=models.CASCADE,
        verbose_name="Сообщение"
    )
    clients = models.ManyToManyField('Client', verbose_name="Получатели")
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Владелец",
        related_name="mailings"
    )

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
            self.save(update_fields=['status'])


# # Модель "Рассылка"
# class Mailing(models.Model):
#     STARTED = "Создана"
#     RUNNING = "Запущена"
#     COMPLETED = "Завершена"
#     STATUS_CHOICES = [
#         (STARTED, "Создана"),
#         (RUNNING, "Запущена"),
#         (COMPLETED, "Завершена"),
#     ]
#
#     DAILY = "Ежедневная"
#     WEEKLY = "Раз в неделю"
#     MONTHLY = "Раз в месяц"
#     PERIOD_CHOICES = [
#         (DAILY, "Ежедневная"),
#         (WEEKLY, "Раз в неделю"),
#         (MONTHLY, "Раз в месяц"),
#     ]
#
#     start_datetime = models.DateTimeField(verbose_name="Дата и время старта")
#     end_datetime = models.DateTimeField(verbose_name="Дата и время окончания")
#     period = models.CharField(
#         max_length=20,
#         choices=PERIOD_CHOICES,
#         blank=True,
#         null=True,
#         verbose_name="Период"
#     )
#     status = models.CharField(
#         max_length=20,
#         choices=STATUS_CHOICES,
#         default=STARTED,
#         verbose_name="Статус"
#     )
#     message = models.ForeignKey("Message", on_delete=models.CASCADE, verbose_name="Сообщение")
#     clients = models.ManyToManyField(Client, verbose_name="Клиенты")
#     owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец", related_name="mailings")
#
#     def __str__(self):
#         return f"Рассылка {self.id}: {self.status}"
#
#     class Meta:
#         verbose_name = "Рассылка"
#         verbose_name_plural = "Рассылки"
#
#

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
