from django.db import models

from .base import Base

class Lecturer(Base):
  name = models.CharField(
    unique=True,
    max_length=60
  )

  def __str__(self):
    return self.name
