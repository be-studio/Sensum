from django.db import models
from .base import Base


class Country(Base):
  country = models.CharField(
    max_length=128,
    unique=True
  )
  alt_name = models.CharField(
    max_length=128,
    blank=True
  )
  iso_code = models.CharField(
    max_length=6,
    blank=True
  )


  class Meta:
    verbose_name_plural = "Countries"


class Department(Base):
  department = models.CharField(
    max_length=128,
    unique=True
  )
  description = models.TextField(
    blank=True
  )
