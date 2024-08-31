from django.db import models
from django.utils.timezone import now


class Base(models.Model):
  date_created = models.DateTimeField(
    "Date Created",
    default=now,
    editable=False
  )
  date_updated = models.DateTimeField(
    "Date Updated",
    auto_now=True,
    null=True
  )


  class Meta:
    abstract = True
