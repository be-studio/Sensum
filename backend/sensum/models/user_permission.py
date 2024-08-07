from django.db import models
from django.utils.timezone import now
from .base import Base


class UserPermission(Base):
  permission = models.CharField(max_length=32)
  alias = models.CharField(max_length=64)
  description = models.TextField(blank=True, null=True)
  comments = models.TextField(blank=True, null=True)
