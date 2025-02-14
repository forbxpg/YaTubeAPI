"""Вьюсеты для API."""
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, mixins
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from posts.models import (
    Post, Group
)
from .permissions import OnlyAuthorPermission
from .serializers import (
    CommentSerializer, FollowSerializer,
    GroupSerializer, PostSerializer
)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для модели Group."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.AllowAny,)


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (OnlyAuthorPermission,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user
        )


class FollowViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """Вьюсет для модели Follow."""

    serializer_class = FollowSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('following__username', 'user__username')

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Comment."""

    serializer_class = CommentSerializer
    permission_classes = (OnlyAuthorPermission,)

    def get_queryset(self):
        post = get_object_or_404(
            Post, pk=self.kwargs['post_id']
        )
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(
            Post, pk=self.kwargs['post_id']
        )
        serializer.save(
            author=self.request.user, post=post
        )
