from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    name = models.CharField(verbose_name="Название", max_length=128)
    description = models.TextField(verbose_name="Описание")
    done = models.BooleanField(verbose_name="Завершено", default=False)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return f"Пользователь: {self.user.username}, имя задачи: {self.name}"
