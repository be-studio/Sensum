from django.db import models
from django.contrib.auth.models import User

from .base import Base
from .event import Event

class Seat(Base):
  user = models.OneToOneField(
    User,
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
