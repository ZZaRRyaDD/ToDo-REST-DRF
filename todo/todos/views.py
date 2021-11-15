from rest_framework import generics, permissions
from . import serializers, models
from django.db.models import Q


class TaskCreateView(generics.CreateAPIView):
    serializer_class = serializers.TaskDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskRetrieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TaskDetailSerializer
    queryset = models.Task.objects.all()
    permission_classes = (permissions.IsAuthenticated, )


class UserTasksView(generics.ListAPIView):
    serializer_class = serializers.TaskDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.kwargs['pk']
        return models.Task.objects.filter(user__id=user)


class SearchListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = serializers.TaskDetailSerializer

    def get_queryset(self):
        queryset = None
        keywords = self.request.GET.get('search')
        if keywords:
            queryset = models.Task.objects.filter(Q(name__icontains=keywords)
                                                  | Q(description__icontains=keywords))
        return queryset
