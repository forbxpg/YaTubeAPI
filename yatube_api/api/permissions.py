"""Модуль, содержащий классы разрешений для API."""
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
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
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
