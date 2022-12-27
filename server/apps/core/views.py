from rest_framework import mixins, viewsets

from .services.pagination import PaginationObject


class BaseViewSet(viewsets.ModelViewSet):
    """Base ViewSet for other views."""

    pagination_class = PaginationObject


class CreateUpdateDeleteViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """ViewSet for `create`, `update` and `destroy` actions."""
