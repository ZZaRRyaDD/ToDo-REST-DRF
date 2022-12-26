from django.db.models import Q
from rest_framework import generics, permissions
from wall.permissions import IsCreator

from . import serializers, models


class TaskCreateView(generics.CreateAPIView):
    """Создание задачи"""
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.TaskCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskRetrieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Обновление / удаление / просмотр задачи"""
    permission_classes = [permissions.IsAuthenticated, IsCreator]
    serializer_class = serializers.TaskCreateSerializer
    queryset = models.Task.objects.all()


class SearchListView(generics.ListAPIView):
    """Поиск задач по введенному запросу"""
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.TaskDetailSerializer

    def get_queryset(self):
        queryset = []
        keywords = self.request.GET.get('search')
        if keywords:
            for keyword in keywords:
                keyword_queryset = list(
                    models.Task.objects.filter(
                        Q(name__icontains=keyword) |
                        Q(description__icontains=keyword)
                    )
                )
                if keyword_queryset:
                    queryset.extend(keyword_queryset)
        return list(set(queryset))
