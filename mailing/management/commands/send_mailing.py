from django.core.management.base import BaseCommand
from mailing.models import Mailing


# Запуск из консоли:
# python manage.py send_mailing 1
# (где 1 — ID рассылки)

class Command(BaseCommand):
    help = 'Отправляет рассылку по ID'

    def add_arguments(self, parser):
        parser.add_argument('mailing_id', type=int, help='ID рассылки для отправки')


    def handle(self, *args, **options):
        mailing_id = options['mailing_id']
        try:
            mailing = Mailing.objects.get(pk=mailing_id)
            mailing.send_mailing()
            self.stdout.write(
                self.style.SUCCESS(f'Рассылка {mailing_id} запущена!')
            )
        except Mailing.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(f'Рассылка с ID {mailing_id} не найдена.')
            )
        except ValueError as e:
            self.stdout.write(self.style.ERROR(f'Ошибка: {e}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при отправке: {e}'))
