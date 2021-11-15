from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class TaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Task
        fields = ['name', 'description', 'done']


class TaskDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Task
        fields = "__all__"
