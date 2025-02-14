"""Модуль, содержащий классы разрешений для API."""
from rest_framework import permissions


class OnlyAuthorPermission(permissions.BasePermission):
    """
    Класс, определяющий разрешения на изменение
    контента только для автора этого контента.
    """

    def has_permission(self, request, view):
        """Проверка на аутентификацию пользователя.

        Возвращает True, если пользователь аутентифицирован
        или метод запроса входит в список безопасных.
        """
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        """Проверка на авторство объекта.

        Возвращает True, если пользователь является автором
        или метод запроса входит в список безопасных.
        """
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
