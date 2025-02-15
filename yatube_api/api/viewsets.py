from rest_framework import viewsets, mixins


class CreateListViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """Базовый вьюсет для создания и просмотра моделей."""
