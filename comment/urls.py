from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.views import APIView

from .views import CommentsViewSet, ModelCommentsList, CustomeCommentView

router = routers.DefaultRouter()
router.register(r'comments', CommentsViewSet)
router.register(r'get', CustomeCommentView)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^comments/get_comments/(?P<pk>[^/.]+)$', ModelCommentsList.as_view()),
    # url(r'^get/', CustomeCommentView.as_view())
]