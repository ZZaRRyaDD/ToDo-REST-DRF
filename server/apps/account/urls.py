from django.urls import include, path

from . import views

urlpatterns = [
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("<int:pk>/posts/", views.PostsUserView.as_view(), name="user_posts"),
    path("<int:pk>/todo/", views.TasksUserView.as_view(), name="user_tasks"),
]
