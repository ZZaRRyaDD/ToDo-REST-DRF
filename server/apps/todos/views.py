from rest_framework import permissions

from apps.core.views import CreateUpdateDeleteViewSet
from apps.wall.permissions import IsCreator

from . import models, serializers


class TaskViewSet(CreateUpdateDeleteViewSet):
    """ViewSet for task."""

    permission_classes = (permissions.IsAuthenticated, IsCreator)
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
