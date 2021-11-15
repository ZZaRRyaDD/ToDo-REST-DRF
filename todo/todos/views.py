from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from . import serializers, models
from django.db.models import Q


class TaskCreateView(generics.CreateAPIView):
    serializer_class = serializers.TaskCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.TaskCreateSerializer
    queryset = models.Task.objects.all()
    permission_classes = (IsAuthenticated, )


class TaskRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = serializers.TaskDetailSerializer
    queryset = models.Task.objects.all()
    permission_classes = (IsAuthenticated, )


class UserTasksView(generics.ListAPIView):
    serializer_class = serializers.TaskCreateSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.kwargs['pk']
        return models.Task.objects.filter(user__id=user)


class SearchListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.TaskDetailSerializer

    def get_queryset(self):
        queryset = None
        keywords = self.request.GET.get('search')
        if keywords:
            queryset = models.Task.objects.filter(Q(name__icontains=keywords)
                                                  | Q(description__icontains=keywords))
        return queryset
