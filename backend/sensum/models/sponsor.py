from django.db import models

from .base import Base


class Sponsor(Base):
  name = models.CharField(
    unique=True,
    max_length=30
  )
  logo = models.CharField(
    max_length=300
  )
  link = models.CharField(
    max_length=300
  )


  def __str__(self):
    return self.name
