from account.serializers import UserSerializer
from rest_framework import serializers

from . import models


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ["text", ]


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.Comment
        fields = ["id", "date_time", "user", "post", "text"]
        read_only_fields = ["user", ]


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ["task", ]


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.Post
        fields = ["id", "date_time", "task", "user"]
        read_only_fields = ["user", ]
