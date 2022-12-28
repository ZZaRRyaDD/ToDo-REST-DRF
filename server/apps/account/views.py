from rest_framework import generics, permissions

from apps.todos.models import Task
from apps.todos.serializers import TaskSerializer
from apps.wall.models import Post
from apps.wall.serializers import PostSerializer


class PostsUserView(generics.ListAPIView):
    """View for get posts of user."""

    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.select_related("user").filter(
            user__id=self.kwargs['pk'],
        )


class TasksUserView(generics.ListAPIView):
    """View for get tasks of user."""

    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.select_related("user").filter(
            user__id=self.kwargs['pk'],
        )
