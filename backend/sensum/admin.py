from django.contrib import admin

from .models import Course, Lecturer, Event, Seat, Offer, Sponsor, CourseAdditionalInfo

class EventInline(admin.TabularInline):
  model = Event

class CourseAdmin(admin.ModelAdmin):
  fieldSets = (
    ("None", {
      "fields": (
        "title",
        "primary_subtitle",
        "secondary_subtitle",
        "duration",
        "audience_groups",
        "lecturers",
        "sponsors",
        "about_description",
        "additional_info"
      )
    }),
  )
  inlines = [
    EventInline
  ]

admin.site.register(Course, CourseAdmin)
admin.site.register([
  Lecturer,
  Event,
  Seat,
  Offer,
  Sponsor,
  CourseAdditionalInfo
])
