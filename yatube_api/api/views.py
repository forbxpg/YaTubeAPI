"""Вьюсеты для API."""
from rest_framework import (
    viewsets, permissions,
    pagination, filters,
)

from posts.models import (
    Post, Group, Comment, Follow
)
from .serializers import (
    CommentSerializer, FollowSerializer,
    GroupSerializer, PostSerializer
)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.AllowAny,)


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Post."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class FollowViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Follow."""
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Comment."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
