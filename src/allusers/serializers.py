from rest_framework import serializers
from .models import AllUser

class AllUsersSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AllUser
        fields = ('url', 'username', 'password', 'first_name', 'last_name', 'email_address')