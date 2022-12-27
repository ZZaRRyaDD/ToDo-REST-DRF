from django.shortcuts import get_object_or_404
from rest_framework import decorators, permissions

from apps.core.views import BaseViewSet, CreateUpdateDeleteViewSet

from . import models
from . import permissions as perm
from . import serializers


class PostViewSet(BaseViewSet):
    """ViewSet for post."""

    permission_classes = (permissions.IsAuthenticated, perm.IsCreator)

    def get_queryset(self):
        if self.action == "comments":
            return get_object_or_404(
                models.Post.objects.prefetch_related("comments"),
                pk=self.kwargs["pk"],
            ).comments.all()
        return models.Post.objects.select_related(
            "task",
            "user",
        ).order_by('-created_at')

    def get_serializer_class(self):
        if self.action == "comments":
            return serializers.CommentSerializer
        return serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @decorators.action(methods=("GET",), detail=True)
    def comments(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class CommentViewSet(CreateUpdateDeleteViewSet):
    """ViewSet for comment."""

    permission_classes = (permissions.IsAuthenticated, perm.IsCreator)
    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
