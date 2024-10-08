from django.db import models

from .base import Base


class CourseAdditionalInfo(Base):
  title = models.CharField(
    max_length=120
  )
  description = models.TextField()

  def __str__(self):
    return self.title
