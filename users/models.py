from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name="UUID")
    username = models.CharField(unique=True, max_length=64, null=True, verbose_name="имя пользователя")
    first_name = models.CharField(max_length=64, blank=True, verbose_name="имя")
    last_name = models.CharField(max_length=64, blank=True, verbose_name="фамилия")
    birthday_year = models.PositiveIntegerField(null=True, blank=True, verbose_name="год рождения")
    email = models.CharField(
        max_length=256,
        unique=True,
        null=False,
        verbose_name="электронная почта",
        error_messages={
            "unique": "A user with that email address already exists.",
        },
    )

    def __str__(self):
        return f"{self.username} | {self.first_name} {self.last_name}"
