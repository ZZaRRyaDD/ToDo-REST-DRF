from datetime import date
from tempfile import NamedTemporaryFile

from django.core.files.base import ContentFile
from django.http import HttpResponse
from rest_framework import decorators, permissions, response, status

from apps.core.services import export_operation, import_tasks
from apps.core.views import CreateUpdateDeleteViewSet
from apps.wall.permissions import IsCreator

from . import models, serializers


class TaskViewSet(CreateUpdateDeleteViewSet):
    """ViewSet for task."""

    permission_classes = (permissions.IsAuthenticated, IsCreator)
    serializer_class = serializers.TaskSerializer

    def get_queryset(self):
        if self.action == "export_tasks":
            return models.Task.objects.filter(user_id=self.request.user.id)
        return models.Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @decorators.action(methods=("GET",), detail=False, url_path="export")
    def export_tasks(self, request, *args, **kwargs):
        with NamedTemporaryFile() as file_obj:
            export_operation(
                self.get_queryset(),
                file_obj.name,
            )
            file_to_send = ContentFile(file_obj.read())
            filename = f'Tasks-{request.user.username}-{date.today()}'
            http_response = HttpResponse(file_to_send, 'application/x-gzip')
            http_response['Content-Length'] = file_to_send.size
            http_response['Content-Disposition'] = (
                f'attachment; filename="{filename}.csv"'
            )
            http_response['Access-Control-Expose-Headers'] = 'Content-Disposition'
            return http_response

    @decorators.action(methods=("POST",), detail=False, url_path="import")
    def import_tasks(self, request, *args, **kwargs):
        data = import_tasks(request)
        if 'message' not in data:
            return response.Response(
                data=data,
                status=status.HTTP_201_CREATED,
            )
        return response.Response(
            data=data,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
