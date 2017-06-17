from rest_framework import serializers
from .models import Comment

class CommentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('url', 'post', 'user', 'content', 'updated', 'timestamp')