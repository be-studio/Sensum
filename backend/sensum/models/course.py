from django.db import models
from django.contrib.auth.models import Group

from .base import Base
from .lecturer import Lecturer
from .sponsor import Sponsor
from .course_additional_info import CourseAdditionalInfo

class Course(Base):
  title = models.CharField(
    unique=True,
    max_length=120
  )
  primary_subtitle = models.CharField(
    blank=True,
    max_length=500,
  )
  secondary_subtitle = models.CharField(
    blank=True,
    max_length=500,
  )
  duration = models.DurationField(
    blank=True,
    null=True
  )
  audience_groups = models.ManyToManyField(
    Group,
    verbose_name="Audience Groups"
  )
  lecturers = models.ManyToManyField(Lecturer)
  sponsors = models.ManyToManyField(Sponsor)
  about_description = models.TextField()
  additional_info = models.OneToOneField(
    CourseAdditionalInfo,
    on_delete=models.CASCADE,
    null=True
  )

  def __str__(self):
    return self.title
