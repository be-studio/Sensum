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
    desc_limit = 20
    return f"{self.price} - {(self.description[:desc_limit] + "...") if len(self.description) > desc_limit else self.description}"
