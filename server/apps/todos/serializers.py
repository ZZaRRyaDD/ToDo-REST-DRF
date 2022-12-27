from apps.core.serializers import BaseModelSerializer, serializers

from . import models


class TaskSerializer(BaseModelSerializer):
    """Serializer for Task model."""

    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )

    class Meta:
        model = models.Task
        fields = (
            "id",
            "name",
            "description",
            "done",
            "user",
        )
