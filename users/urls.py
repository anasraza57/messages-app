from django.urls import path
from .views import RegisterAPI, Logout, UserViewSet
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register', RegisterAPI.as_view(), name='register'),
    path('login', obtain_auth_token, name='api_token_auth'),
    path('logout', Logout.as_view(), name='logout'),
    path('users', UserViewSet.as_view(), name='users'),
]


