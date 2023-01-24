from rest_framework import generics
from application.serializers import UserSerializer


class UserViewset(generics.CreateAPIView):
    serializer_class = UserSerializer