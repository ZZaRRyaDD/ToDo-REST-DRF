from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """Model of Post."""

    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата создания поста",
    )
    task = models.ForeignKey(
        "todos.Task",
        on_delete=models.CASCADE,
        related_name="task",
        verbose_name="Задача",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Автор",
    )
    text = models.TextField(
        default="",
        verbose_name="Текст к посту",
    )

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return f"id: {self.id}, составитель: {self.user.username}, задача: {self.task.name}"


class Comment(models.Model):
    """Model of Comment."""

    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата создания поста",
    )
    text = models.TextField(
        default="",
        verbose_name="Текст комментария",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Автор",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Пост комментария",
    )

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"Отправитель: {self.user.username}, текст: {self.text}"
