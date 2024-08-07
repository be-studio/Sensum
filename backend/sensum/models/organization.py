from django.db import models

from .base import Base
from .locations import Country


class Organization(Base):
  name = models.CharField(
    max_length=128,
    unique=True
  )
  avatar = models.CharField(
    max_length=512,
    blank=True,
    null=True
  )
  email = models.EmailField(
    max_length=255,
    blank=True,
    null=True
  )
  address_street_1 = models.CharField(
    max_length=128,
    blank=True,
    null=True
  )
  address_street_2 = models.CharField(
    max_length=128,
    blank=True,
    null=True
  )
  address_street_3 = models.CharField(
    max_length=128,
    blank=True,
    null=True
  )
  settlement = models.CharField(
    max_length=128,
    blank=True,
    null=True
  )
  locality = models.CharField(
    max_length=128,
    blank=True,
    null=True
  )
  postal_code = models.CharField(
    max_length=128,
    blank=True,
    null=True
  )
  country = models.ForeignKey(
    Country,
    blank=True,
    null=True,
    on_delete=models.CASCADE,
    related_name="country_country"
  )
  website = models.CharField(
    max_length=255,
    blank=True,
    null=True
  )
  landline_phone = models.CharField(
    max_length=20,
    blank=True,
    null=True
  )
  extension = models.CharField(
    max_length=8,
    blank=True,
    null=True
  )
  mobile_phone = models.CharField(
    max_length=20,
    blank=True,
    null=True
  )
