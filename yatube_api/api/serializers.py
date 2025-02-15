"""Модуль, определяющий классы сериализаторов моделей."""
import base64
from django.core.files.base import ContentFile
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import (
    Comment, Follow,
    Group, Post, User
)


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор модели поста."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = (
            'id',
            'text',
            'pub_date',
            'author',
            'image',
            'group',
        )
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор модели комментария."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = (
            'id',
            'text',
            'created',
            'author',
            'post',
        )
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор модели Group."""

    class Meta:
        fields = (
            'id',
            'title',
            'slug',
            'description',
        )
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Follow."""

    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        fields = (
            'user',
            'following',
        )
        model = Follow
        read_only_fields = ('user',)
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Вы уже подписаны на этого пользователя'
            )
        ]

    def validate_following(self, value):
        if value == self.context['request'].user:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя'
            )
        return value
