from django.core.management.base import BaseCommand, CommandError
from auth_app.models import User
from os import path
from json import load
from random import randrange

class Command(BaseCommand):
    help = "Обновление списка пользователей"

    def handle(self, *args, **kwargs):
        with open(path.join(
            "media",
            "bd",
            "users.json"
        ), "r+", encoding="utf-8") as f:
            users = load(f)

        for user_id in users:
            _id = user_id
            data = {
                "username": users[_id]["username"],
                "password": users[_id]["password"],
                "email": users[_id]["email"],
                "first_name": users[_id]["first_name"],
                "desc": users[_id]["desc"],
                "age": users[_id]["age"],
            }

            User.objects.update_or_create(
                id=_id,
                defaults=data,
            )
