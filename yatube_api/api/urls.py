from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('groups', views.GroupViewSet, basename='groups')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
]
