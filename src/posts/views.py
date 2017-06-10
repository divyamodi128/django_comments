from django.shortcuts import render
from rest_framework import viewsets, generics, mixins, permissions
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from collections import OrderedDict

from .models import Post
from .serializers import PostSerializers

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
    
    @detail_route(methods=['get'])
    def get_comments(self, request, pk=None):
        queryset = Post.objects.get(id=pk)
        post_serializer = PostSerializers(queryset, context={'request': request})
        comments = request.get('http://127.0.0.1:8000/comments/')
        context = OrderedDict({
            'comments': comments,
            'post': post_serializer.data,
        })
        return Response(context)
