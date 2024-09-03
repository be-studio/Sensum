from django.db import models

from .base import Base
from .course import Course


class Event(Base):
  title = models.CharField(
    unique=True, max_length=60
  )
  subtitle = models.CharField(
    blank=True, max_length=120
  )
  time = models.TimeField(
    blank=True
  )
  date = models.DateField(
    blank=True
  )
  location = models.CharField(
    blank=True, max_length=90
  )
  course = models.ForeignKey(
    Course, on_delete=models.CASCADE, blank=True, null=True
  )

  def __str__(self):
    return self.title
