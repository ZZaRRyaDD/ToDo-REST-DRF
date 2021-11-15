from django.urls import path, include
from . import views


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('activate/<uid>/<token>/', views.UserActivationView.as_view(), name="activate_user"),
    path('reset/password/confirm/<uid>/<token>/', views.PasswordResetView.as_view(), name="activate_user"),
    path('logout/', views.LogoutAPIView.as_view(), name="logout"),
]