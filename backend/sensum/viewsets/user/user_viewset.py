from rest_framework import viewsets, permissions
from django.conf import settings
from django.contrib.auth import get_user_model

from ...serializers.user.user_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer
  permission_classes = (permissions.IsAuthenticated,)
