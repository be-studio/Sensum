from django.contrib import admin
from django.contrib.auth import get_user_model
from django import forms
from .models import Course, Lecturer, Event, Seat, Offer, Sponsor, CourseAdditionalInfo
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
  """A form for creating new users. Includes all the required fields plus a
  repeated password.
  """
  password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
  password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)


  class Meta:
    model = get_user_model()
    fields = ("email",)


  def clean_password2(self):
    """
    :return:
    :rtype:
    """
    # Check that the two password entries match.
    password1 = self.cleaned_data.get("password1")
    password2 = self.cleaned_data.get("password2")

    if password1 and password2 and password1 != password2:
      raise forms.ValidationError("Passwords don't match")
    return password2


  # noinspection PyShadowingNames
  def save(self, commit=True):
    """
    :param commit:
    :type commit: bool
    :return:
    :rtype:
    """
    # Save the provided password in hashed format.
    user = super().save(commit=False)
    user.set_password(self.cleaned_data["password1"])
    if commit:
      user.save()
    return user


class UserChangeForm(forms.ModelForm):
  """A form for updating users. Includes all the fields on the user, but
  replaces the password field with the admin's password hash display field.
  """
  password = ReadOnlyPasswordHashField()


  class Meta:
    model = get_user_model()
    fields = ('email', 'password', 'is_active', 'is_staff')


  def clean_password(self):
    """
    :return:
    :rtype:
    """
    # Regardless of what the user provides, return the initial value.
    # This is done here, rather than on the field, because the
    # field does not have access to the initial value
    return self.initial["password"]


class EventInline(admin.TabularInline):
  model = Event

class UserEventsInline(admin.TabularInline):
  model = get_user_model().events.through

class UserAdmin(BaseUserAdmin):
  # The forms to add and change user instances
  form = UserChangeForm
  add_form = UserCreationForm

  # The fields to be used in displaying the User model.
  # These override the definitions on the base `UserAdmin` that reference
  # specific fields on `auth.User`.
  list_display = ("email", "is_staff", "last_login")
  list_filter = ("is_staff",)
  fieldsets = (
    (None, {
      "fields": (
        "email",
        "password",
        "title",
        "first_name",
        "last_name",
        "mobile_phone",
        "landline_phone",
        "extension",
        "last_app_login",
      )
    }),
    ("Permissions", {
      "fields": ("is_staff",)
    }),
  )
  inlines = [
    UserEventsInline
  ]
  readonly_fields = ("last_app_login",)
  # `add_fieldsets` is not a standard `ModelAdmin` attribute. `UserAdmin`
  # overrides `get_fieldsets` to use this attribute when creating a user.
  add_fieldsets = (
    (None, {
      "classes": ("wide",),
      "fields": ("email", "password1", "password2"),
    }),
  )
  search_fields = ("email",)
  ordering = ("email",)
  filter_horizontal = ()

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

class EventAdmin(admin.ModelAdmin):
  inlines= [
    UserEventsInline
  ]

admin.site.register(get_user_model(), UserAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register([
  Lecturer,
  Seat,
  Offer,
  Sponsor,
  CourseAdditionalInfo
])
