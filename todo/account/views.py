from django.contrib.auth.models import User
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from todos.models import Task
from todos.serializers import TaskDetailSerializer
from wall.models import Post
from wall.serializers import PostSerializer

from . import serializers


class LogoutAPIView(generics.GenericAPIView):
    """Выход"""
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.LogoutSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "Пользователь вышел"},
                        status=status.HTTP_204_NO_CONTENT)


class PostsUserView(generics.ListAPIView):
    """Просмотр постов пользователя"""
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(user__id=self.kwargs['pk'])


class TasksUserView(generics.ListAPIView):
    """Просмотр задач пользователя"""
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = TaskDetailSerializer

    def get_queryset(self):
        return Task.objects.filter(user__id=self.kwargs['pk'])


class InfoOtherUserView(generics.RetrieveAPIView):
    """Просмотр информации о другом юзере"""
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
