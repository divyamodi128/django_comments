from django.shortcuts import render
from rest_framework import viewsets, generics, mixins, permissions
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializers
from comment.models import Comment

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Optionally we can also provide an extra `methods` action.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
                        #   IsOwnerOrReadOnly,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    @detail_route()
    def get_comments(self, request, pk=None):
        queryset = Post.objects.get(id=pk)
        post_serializer = PostSerializers(queryset, context={'request': request})
        comment_queryset = Comment.objects.filter(post=queryset)
        comment_serializer = self.serializer_class(comment_queryset, many=True, context={'request': request})
        context = {
            'post': post_serializer.data,
            'comments': comment_serializer.data
        }
        return Response(context)
