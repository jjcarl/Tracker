from django.shortcuts import render
from main.models import Area, Point
from main.serializers import AreaSerializer, UserSerializer, PointSerializer
from main.permissions import IsOwnerOrReadOnly
from rest_framework import renderers, viewsets, permissions
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import detail_route


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_class = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
    permission_class = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
