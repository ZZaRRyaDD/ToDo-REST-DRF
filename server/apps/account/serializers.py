from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model."""

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_active",
            "date_joined",
            "last_login",
            "password",
        )
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        user = None
        if not User.objects.filter(email=validated_data["email"]).exists():
            user = User.objects.create_user(**validated_data)
            user.is_active = False
            user.save()
        return user
