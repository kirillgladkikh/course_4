from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from mailing.models import Client, Mailing, Log

class Command(BaseCommand):
    help = 'Создаёт группы ролей и назначает разрешения'

    def handle(self, *args, **options):
        # Группа "Пользователь"
        user_group, created = Group.objects.get_or_create(name='Пользователь')
        if created:
            self.stdout.write('Создана группа "Пользователь"')

        # Разрешения для пользователей (только свои объекты)
        client_ct = ContentType.objects.get_for_model(Client)
        mailing_ct = ContentType.objects.get_for_model(Mailing)
        log_ct = ContentType.objects.get_for_model(Log)

        permissions = [
            ('add_client', client_ct),
            ('change_client', client_ct),
            ('delete_client', client_ct),
            ('view_client', client_ct),
            ('add_mailing', mailing_ct),
            ('change_mailing', mailing_ct),
            ('delete_mailing', mailing_ct),
            ('view_mailing', mailing_ct),
            ('view_log', log_ct),
        ]

        for codename, ct in permissions:
            try:
                permission = Permission.objects.get(codename=codename, content_type=ct)
                user_group.permissions.add(permission)
            except Permission.DoesNotExist:
                self.stdout.write(f'Разрешение {codename} не найдено')

        # Группа "Менеджер" — суперпользователи имеют все права автоматически
        manager_group, created = Group.objects.get_or_create(name='Менеджер')
        if created:
            self.stdout.write('Создана группа "Менеджер"')
