from rest_framework.serializers import HyperlinkedModelSerializer
from django.core import serializers
from .models import Comment
from django.contrib.auth.models import User
# from django.conf import settings
from src.views import UserSerializer
from posts.serializers import PostSerializers

# from src.views import UserSerializer
# from django.contrib.auth.models import User
# from selectable.base import ModelLookup
# from selectable.decorators import login_required
# from selectable.registry import registry

# class UserLookup(ModelLookup):
#     model = User
#     search_fields = ('username__icontains', )
#     filters = {'is_active': True, }

# registry.register(UserLookup)

class CommentListSerializers(HyperlinkedModelSerializer):
    user = UserSerializer()
    custom_model = PostSerializers()

    class Meta:
        model = Comment
        fields = ('id', 'url', 'custom_model', 'user', 'parent_comment', 'content', 'updated', 'timestamp')

class CommentSerializers(HyperlinkedModelSerializer):
    # user = UserSerializer(view_name='user-list')
    # custom_model = PostSerializers(view_name='user-list')

    class Meta:
        model = Comment
        fields = ('id', 'url', 'custom_model', 'user', 'parent_comment', 'content', 'updated', 'timestamp')
