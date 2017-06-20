from rest_framework import serializers
from .models import Comment

class CommentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('url', 'custom_model', 'user', 'content', 'updated', 'timestamp')