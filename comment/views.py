from django.shortcuts import render
from django.apps import apps
from django.contrib.auth import get_user_model
from django.core.signals import setting_changed
from django.dispatch import receiver
from rest_framework import viewsets, permissions
from rest_framework.decorators import detail_route, list_route
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CommentSerializers
from .models import Comment


class CommentsViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the accounts
    associated with the user.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ModelCommentsList(APIView):
    """
    List all Comments for corresponding Model.
    """
    # queryset = Comments.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, pk=None, format=None):
        import pdb; pdb.set_trace()
        comments = Comment.objects.filter(custom_model=pk)
        serializer = CommentSerializers(
            comments, 
            context={'request': request},
            many=True
        )
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CommentSerializers(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
