from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from os import path
from datetime import timedelta


class User(AbstractUser):
    avatar = models.ImageField(verbose_name = "Аватарка",
        blank=True, upload_to=path.join("img", "users", "avatars"))
    username = models.CharField(blank = True, unique = True, verbose_name = "Ник", max_length=250)
    email = models.EmailField(blank = True, verbose_name = "eMail")
    first_name = models.CharField(verbose_name = "ФИО", max_length=250)
    desc = models.CharField(verbose_name= "Описание", max_length=400)
    age = models.PositiveIntegerField(verbose_name = "Возраст")
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(
        default=(now() + timedelta(hours=48)))

    def __str__(self):
        return f"Пользователь: {self.username} (Имя: {self.first_name}, возраст: {self.age})"

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True
