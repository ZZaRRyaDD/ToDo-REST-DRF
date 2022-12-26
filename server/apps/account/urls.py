from django.urls import path, include

from . import views

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('<int:pk>/posts/', views.PostsUserView.as_view(), name="user_posts"),
    path('<int:pk>/user/', views.InfoOtherUserView.as_view(), name="user_info"),
    path('<int:pk>/todos/', views.TasksUserView.as_view(), name="user_tasks"),
]
