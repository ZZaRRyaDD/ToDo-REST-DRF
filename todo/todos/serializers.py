from rest_framework import serializers
from . import models


class TaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Task
        fields = ["name", "description", "done"]


class TaskDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Task
        fields = "__all__"
