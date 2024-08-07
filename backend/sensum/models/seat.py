from django.contrib.auth import get_user_model
from django.db import models

from .base import Base
from .event import Event

class Seat(Base):
  user = models.OneToOneField(
    get_user_model(),
    on_delete=models.PROTECT
  )
  registration_number = models.CharField(
    unique=True,
    max_length=60
  )
  event = models.ForeignKey(
    Event,
    on_delete=models.CASCADE,
    blank=True,
    null=True
  )

  def __str__(self):
    return self.user.get_full_name()
