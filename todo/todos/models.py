from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField(verbose_name="Название", max_length=128)
    description = models.TextField(verbose_name="Описание")
    done = models.BooleanField(verbose_name="Завершено")
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
