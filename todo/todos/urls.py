from django.urls import path
from rest_framework.schemas import get_schema_view

from . import views

urlpatterns = [
    path('create/', views.TaskCreateView.as_view(), name="create_task"),
    path('<int:pk>/', views.TaskRetrieveDestroyView.as_view(), name="urd_task"),
    path('search_task/', views.SearchListView.as_view(), name="task_search"),
]
