from django.conf import settings
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.todos.views import TaskViewSet
from apps.wall.views import CommentViewSet, PostViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("todo", TaskViewSet, basename="todo")
router.register("posts", PostViewSet, basename="posts")
router.register("comments", CommentViewSet, basename="comments")

app_name = "api"
urlpatterns = router.urls + [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="api:schema")),
    path('users/', include('apps.account.urls')),
]
