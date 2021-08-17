from django.core.management.base import BaseCommand, CommandError
from auth_app.models import User

class Command(BaseCommand):
    help = "Создание суперпользователя"

    def handle(self, *args, **kwargs):
        User.objects.create_superuser(
            "Admin",
            "coolAdmin@mail.ru",
            "48375163Vamp",
            age="25",
            first_name="Андрей",
            desc="Best admin in the world!",
        )