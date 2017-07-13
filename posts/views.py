from django.shortcuts import render
from rest_framework import viewsets, generics, mixins, permissions
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
# from rest_framework import renderers
from urllib.request import urlparse, urlopen
import json

from collections import OrderedDict

from .models import Post
from .serializers import PostSerializers
from comment.serializers import CommentSerializers

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
    # For Rendering Template using HTMLRenderer
    # renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @detail_route(methods=['get'])
    def get_comments(self, request, pk=None):
        queryset = Post.objects.get(id=pk)
        post_serializer = PostSerializers(queryset, context={'request': request})
        comments = urlopen('http://127.0.0.1:8000/posts/'+pk+'/get/').read().decode()
        context = OrderedDict({
            'comments': json.loads(comments),
            'post': post_serializer.data,
        })
        return render(request,
            'post_details.html',
            context,
        )
        # return Response(context)
