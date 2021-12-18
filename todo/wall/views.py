from rest_framework import generics, permissions

from . import models, serializers


class PostCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.CreatePostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AllListPostsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.order_by('date_time')


class ReadPostView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()


class DeletePostView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.CreatePostSerializer
    queryset = models.Post.objects.all()


class CommentCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, post=models.Post.objects.get(id=self.kwargs['pk']))


class CommentListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        return models.Comment.objects.filter(post__id=self.kwargs['pk'])


class ReadDeleteUpdateCommentView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        return models.Comment.objects.get(id=self.kwargs['pk'])
