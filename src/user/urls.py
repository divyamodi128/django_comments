from django.conf.urls import url
from .views import Register, Login


urlpatterns = [
    url(r'^register$', Register.as_view(), name='register'),
    url(r'^success$', Login.as_view(), name='login'),
]