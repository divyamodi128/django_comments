from django.conf.urls import url, include
from rest_framework import routers
from allusers.views import AllUsersViewSet

router = routers.DefaultRouter()
router.register(r'allusers', AllUsersViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]