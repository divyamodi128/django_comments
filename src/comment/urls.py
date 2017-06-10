from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from .views import CommentsViewSet

router = routers.DefaultRouter()
router.register(r'comments', CommentsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]