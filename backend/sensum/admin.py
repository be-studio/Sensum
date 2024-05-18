from django.contrib import admin

from .models import Course, Lecturer, Event, Seat, Offer, Sponsor, CourseAdditionalInfo

admin.site.register([
  Course,
  Lecturer,
  Event,
  Seat,
  Offer,
  Sponsor,
  CourseAdditionalInfo
])
