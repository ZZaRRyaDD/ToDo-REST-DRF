from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class UserCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = None
        if not User.objects.filter(email=validated_data["email"]):
            user = User.objects.create_user(
                email=validated_data["email"],
                username=validated_data['username'],
                password=validated_data['password'],
            )
            user.is_active = False
            user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')


class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    re_new_password = serializers.CharField(min_length=6, max_length=68, write_only=True)

    class Meta:
        fields = ('new_password', 're_new_password')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
