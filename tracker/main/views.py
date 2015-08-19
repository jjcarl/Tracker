from django.shortcuts import render
from main.models import Area, Point
from main.serializers import AreaSerializer, UserSerializer, PointSerializer
from main.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework import renderers, viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import detail_route


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = (
        permissions.IsAuthenticated, IsOwnerOrReadOnly,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)


class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class UserRegistration(generics.CreateAPIView):
    serializer_class = UserSerializer


class GetUserInfo(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
