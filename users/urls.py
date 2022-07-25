from django.urls import path, include
from .views import RegisterAPI, Logout, get_users
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register', RegisterAPI.as_view(), name='register'),
    path('login', obtain_auth_token, name='api_token_auth'),
    path('logout', Logout.as_view(), name='logout'),
    path('users', get_users, name='users'),
]


