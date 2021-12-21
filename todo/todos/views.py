from django.db.models import Q
from rest_framework import generics, permissions

from . import serializers, models


class TaskCreateView(generics.CreateAPIView):
    """Создание задачи"""
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.TaskCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskRetrieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Обновление / удаление / просмотр задачи"""
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.TaskDetailSerializer
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
                    models.Task.objects.filter(Q(name__icontains=keyword) | Q(description__icontains=keyword) |
                                               Q(name__icontains=keyword.lower()) | Q(
                        description__icontains=keyword.lower()) |
                                               Q(name__icontains=keyword.upper()) | Q(
                        description__icontains=keyword.upper())))
                if keyword_queryset is not None:
                    queryset.extend(keyword_queryset)
        return list(set(queryset))
