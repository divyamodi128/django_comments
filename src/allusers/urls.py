from django.conf.urls import url
from rest_framework import routers
from .views import AllUsersViewSet

allusers_list = AllUsersViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

allusers_detail = AllUsersViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    # url(r'^$', api_root),
    url(r'^users/$', allusers_list, name='allusers-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', allusers_detail, name='allusers-detail'),
    # url(r'^users/(?P<pk>[0-9]+)/highlight/$', allusers_highlight, name='allusers-highlight'),
])
