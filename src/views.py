from rest_framework import viewsets, serializers, permissions
from django.contrib.auth.models import User

# from django.contrib.auth.models import User
# from selectable.base import ModelLookup
# from selectable.decorators import login_required
# from selectable.registry import registry

# class UserLookup(ModelLookup):
#     model = User
#     search_fields = ('username__icontains', )
#     filters = {'is_active': True, }

# registry.register(UserLookup)

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # username = serializers.HyperlinkedRelatedField(
    #     view_name='user-detail',
    #     lookup_field='username',
    #     read_only=True
    # )
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
