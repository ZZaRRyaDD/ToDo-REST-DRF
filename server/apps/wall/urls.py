from django.urls import path

from . import views

urlpatterns = [
    path('create-post/', views.PostCreateView.as_view(), name="create_post"),
    path('', views.AllListPostsView.as_view(), name="all_list_posts"),
    path('<int:pk>/', views.ReadPostView.as_view(), name="post"),
    path('<int:pk>/delete/', views.DeletePostView.as_view(), name="post_delete"),
    path('<int:pk>/comment/', views.CommentCreateView.as_view(), name="post_comments_create"),
    path('<int:pk>/comments/', views.CommentListView.as_view(), name="post_comments_list"),
    path('<int:pk>/comment/info/', views.ReadDeleteUpdateCommentView.as_view(), name="post_do_comments"),
]
