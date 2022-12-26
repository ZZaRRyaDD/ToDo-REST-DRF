from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    date_time = models.DateTimeField(auto_now=True, verbose_name="Дата создания поста")
    task = models.ForeignKey('todos.Task', on_delete=models.CASCADE, verbose_name="Задача", related_name="task")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", related_name="posts")
    text = models.TextField(verbose_name="Текст к посту", default='')

    def __str__(self):
        return f"id: {self.id}, составитель: {self.user.username}, задача: {self.task.name}"


class Comment(models.Model):
    date_time = models.DateTimeField(auto_now=True, verbose_name="Дата создания поста")
    text = models.TextField(verbose_name="Текст комментария")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    post = models.ForeignKey(Post, models.CASCADE, null=False, blank=False, verbose_name="Пост комментария",
                             related_name="comments")

    def __str__(self):
        return f"Отправитель: {self.user.username}, текст: {self.text}"

    class Meta:
        ordering = ('-date_time',)
