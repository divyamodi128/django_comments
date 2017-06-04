from django.shortcuts import render
from rest_framework import viewsets, generics, mixins, permissions
# from rest_framework.decorators import detail_route
from .serializers import AllUsersSerializers
from .models import AllUser
from .permissions import IsOwnerOrReadOnly

# ViewSets define the view behavior.
class AllUsersViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Optionally we can also provide an extra `methods` action.
    """
    queryset = AllUser.objects.all()
    serializer_class = AllUsersSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
                        #   IsOwnerOrReadOnly,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# class AllUsersDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = AllUser.objects.all()
#     serializer_class = AllUsersSerializers
