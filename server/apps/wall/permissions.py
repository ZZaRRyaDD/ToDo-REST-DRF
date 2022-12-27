from rest_framework import permissions


class IsCreator(permissions.BasePermission):
    """Permission for creator user."""

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
