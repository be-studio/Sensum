from django.db import models

from .base import Base
from .event import Event

class Offer(Base):
  price = models.DecimalField(
    max_digits=7,
    decimal_places=2,
    default=0
  )
  description = models.TextField()
  event = models.ForeignKey(
    Event,
    on_delete=models.CASCADE,
    blank=True,
    null=True
  )

  def __str__(self):
    DESC_LIMIT = 20
    return f"{self.price} - {(self.description[:DESC_LIMIT] + "...") if len(self.description) > DESC_LIMIT else self.description}"
