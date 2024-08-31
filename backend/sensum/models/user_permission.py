from django.db import models
from .base import Base


class UserPermission(Base):
  permission = models.CharField(
    max_length=32
  )
  alias = models.CharField(
    max_length=64
  )
  description = models.TextField(
    blank=True
  )
  comments = models.TextField(
    blank=True
  )
