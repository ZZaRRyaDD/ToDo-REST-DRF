from rest_framework import serializers

from apps.account.serializers import UserSerializer
from apps.todos.models import Task
from apps.todos.serializers import TaskSerializer

from . import models


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model."""

    user = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(
        queryset=models.Post.objects.all(),
    )

    class Meta:
        model = models.Comment
        fields = (
            "id",
            "created_at",
            "user",
            "post",
            "text",
        )


class PostSerializer(serializers.ModelSerializer):
    """Serializer for Post model."""

    user = UserSerializer(read_only=True)
    task = serializers.PrimaryKeyRelatedField(
        queryset=Task.objects.all(),
    )

    class Meta:
        model = models.Post
        fields = (
            "id",
            "user",
            "created_at",
            "task",
            "user",
            "text",
        )

    def validate(self, attrs):
        if models.Post.objects.select_related(
            "task",
        ).filter(task=attrs["task"]).exists():
            raise serializers.ValidationError(
                "Пост с такой задачей уже существует",
            )
        return attrs

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update({"task": TaskSerializer(instance.task).data})
        return data
