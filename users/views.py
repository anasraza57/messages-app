from django.http import JsonResponse
from rest_framework import generics, permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from .models import User


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        user = serializer.save()
        return Response({"message": "User Created Successfully"}, status=status.HTTP_201_CREATED)


class Logout(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


def get_users(request):
    users = list(User.objects.filter(is_active=True).values('id', 'first_name', 'last_name'))
    return JsonResponse(users, safe=False, status=status.HTTP_200_OK)
