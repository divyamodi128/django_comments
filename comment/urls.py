from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.views import APIView

from .views import CommentsViewSet, ModelCommentsList, CustomerCommentView


router = routers.DefaultRouter()
router.register(r'comments', CommentsViewSet)
router.register(r'posts/(?P<post>[^/.]+)/get', CustomerCommentView)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^comments/get_comments/(?P<pk>[^/.]+)$', ModelCommentsList.as_view()),
    # url(r'^get/', CustomerCommentView.as_view())
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]