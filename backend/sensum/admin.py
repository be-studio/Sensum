from django.contrib import admin

from .models import Course, Lecturer, Sponsor

admin.site.register(Course)
admin.site.register(Lecturer)
admin.site.register(Sponsor)
