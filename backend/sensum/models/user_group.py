from django.db import models
from .user_permission import UserPermission
from .base import Base


class UserGroup(Base):
  group = models.CharField(
    max_length=32
  )
  permissions = models.ManyToManyField(UserPermission)
  alias = models.CharField(
    max_length=64
  )
  description = models.TextField(
    blank=True
  )
  comments = models.TextField(
    blank=True
  )
