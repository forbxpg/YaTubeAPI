from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import (
    Comment, Post,
    Group, Follow
)


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
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


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group."""

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

    class Meta:
        fields = (
            'user',
            'following',
        )
        model = Follow
