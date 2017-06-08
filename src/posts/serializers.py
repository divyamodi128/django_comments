from rest_framework import serializers
from .models import Post

class PostSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('url', 'title', 'content', 'timestamp', 'updated', 'media_url')

'''4703635512 
ygnesha


ranga 510 771 9301 '''