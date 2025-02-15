"""Модуль, содержащий классы разрешений для API."""
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    SAFE_METHODS
)


class IsAuthorOrReadOnly(IsAuthenticatedOrReadOnly):
    """
    Класс, определяющий разрешения на изменение
    контента только для автора этого контента.
    """

    def has_object_permission(self, request, view, obj):
        """Проверка на авторство объекта.

        Возвращает True, если пользователь является автором
        или метод запроса входит в список безопасных.
        """
        return (
            request.method in SAFE_METHODS
            or obj.author == request.user
        )
