from rest_framework import mixins, viewsets


class BaseViewSet(viewsets.ModelViewSet):
    """Base ViewSet for other views."""


class CreateUpdateDeleteViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """ViewSet for `create`, `update` and `destroy` actions."""
