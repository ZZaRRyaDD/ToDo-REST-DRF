from account.serializers import UserSerializer
from todos.serializers import TaskDetailSerializer
from rest_framework import serializers

from . import models


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ("text", )


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.Comment
        fields = ("id", "date_time", "user", "post", "text")
        read_only_fields = ("user", "id")


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ("task", "text")


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    task = TaskDetailSerializer()

    class Meta:
        model = models.Post
        fields = ("user", "id", "date_time", "task", "user", "text")
        read_only_fields = ("user", "id")
