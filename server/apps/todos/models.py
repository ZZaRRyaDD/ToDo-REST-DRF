from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    """Model of Task."""

    name = models.CharField(
        max_length=128,
        default="",
        verbose_name="Название",
    )
    description = models.TextField(
        default="",
        verbose_name="Описание",
    )
    is_done = models.BooleanField(
        default=False,
        verbose_name="Завершено",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks",
        verbose_name="Пользователь",
    )

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return f"Пользователь: {self.user.username}, имя задачи: {self.name}"
