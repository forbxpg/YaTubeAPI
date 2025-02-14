"""URLs для API."""
from django.urls import path, include
from rest_framework import routers

from . import views

v1_router = routers.DefaultRouter()
v1_router.register('groups', views.GroupViewSet, basename='groups')
v1_router.register('posts', views.PostViewSet, basename='posts')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    views.CommentViewSet, basename='comments'
)
v1_router.register('follow', views.FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt'))
]
