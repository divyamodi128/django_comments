from django.shortcuts import render
from django.apps import apps
from django.contrib.auth import get_user_model
from django.core.signals import setting_changed
from django.dispatch import receiver
from rest_framework import viewsets, permissions

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


# @receiver(setting_changed)
# def user_model_swapped(**kwargs):
#     if kwargs['setting'] == 'AUTH_USER_MODEL':
#         apps.clear_cache()
#         from myapp import some_module
#         some_module.UserModel = get_user_model() 
# Create your views here.
