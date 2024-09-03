from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from .base import Base
from .user_group import UserGroup
from .locations import Department, Country
from .organization import Organization
from .event import Event


class Title(Base):
  title = models.CharField(
    max_length=12, unique=True
  )


class JobTitle(Base):
  job_title = models.CharField(
    max_length=128, unique=True
  )
  description = models.TextField(
    blank=True
  )


  class Meta:
    verbose_name = "Job Title"
    verbose_name_plural = "Job Titles"


class UserManager(BaseUserManager):
  def create_user(self, email, first_name, last_name, password, commit=True):
    """
    Creates and saves a User with the given email, first name, last name
    and password.
    """
    if not email:
      raise ValueError(_('Users must have an email address'))
    if not first_name:
      raise ValueError(_('Users must have a first name'))
    if not last_name:
      raise ValueError(_('Users must have a last name'))

    user = self.model(
      email=self.normalize_email(email), first_name=first_name, last_name=last_name, )

    user.set_password(password)
    if commit:
      user.save(using=self._db)
    return user

  def create_superuser(self, email, first_name, last_name, password):
    """
    Creates and saves a superuser with the given email, first name,
    last name and password.
    """
    user = self.create_user(email, password=password, first_name=first_name, last_name=last_name, commit=False)
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)
    return user


class User(AbstractBaseUser):
  email = models.EmailField(
    verbose_name=_('email address'), max_length=255, unique=True
  )
  # password field supplied by AbstractBaseUser
  # last_login field supplied by AbstractBaseUser
  first_name = models.CharField(_('first name'), max_length=30, blank=True)
  last_name = models.CharField(_('last name'), max_length=150, blank=True)

  is_active = models.BooleanField(
    _('active'), default=True, help_text=_(
      'Designates whether this user should be treated as active. '
      'Unselect this instead of deleting accounts.'
    ), )
  is_staff = models.BooleanField(
    _('staff status'), default=False, help_text=_(
      'Designates whether the user can log into this admin site.'
    ), )
  # is_superuser field provided by PermissionsMixin
  # groups field provided by PermissionsMixin
  # user_permissions field provided by PermissionsMixin

  date_joined = models.DateTimeField(
    _('date joined'), default=timezone.now
  )

  # CUSTOM USER FIELDS
  user_groups = models.ManyToManyField(UserGroup, related_name="users")
  title = models.ForeignKey(Title, blank=True, null=True, on_delete=models.CASCADE)
  job_title = models.ForeignKey(JobTitle, blank=True, null=True, on_delete=models.CASCADE)
  department = models.ForeignKey(Department, blank=True, null=True, on_delete=models.CASCADE)
  organization = models.ForeignKey(
    Organization, blank=True, null=True, on_delete=models.CASCADE, related_name="users"
  )
  landline_phone = models.CharField(max_length=20, blank=True, null=True)
  extension = models.CharField(max_length=8, blank=True, null=True)
  mobile_phone = models.CharField(max_length=20, blank=True, null=True)
  home_address_street_1 = models.CharField(max_length=128, blank=True, null=True)
  home_address_street_2 = models.CharField(max_length=128, blank=True, null=True)
  home_address_street_3 = models.CharField(max_length=128, blank=True, null=True)
  home_settlement = models.CharField(max_length=128, blank=True, null=True)
  home_locality = models.CharField(max_length=128, blank=True, null=True)
  home_postal_code = models.CharField(max_length=20, blank=True, null=True)
  home_country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.CASCADE, related_name="home_country_country")
  business_address_street_1 = models.CharField(max_length=128, blank=True, null=True)
  business_address_street_2 = models.CharField(max_length=128, blank=True, null=True)
  business_address_street_3 = models.CharField(max_length=128, blank=True, null=True)
  business_settlement = models.CharField(max_length=128, blank=True, null=True)
  business_locality = models.CharField(max_length=128, blank=True, null=True)
  business_postal_code = models.CharField(max_length=20, blank=True, null=True)
  business_country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.CASCADE, related_name="business_country_country")
  website = models.CharField(max_length=256, blank=True, null=True)
  emergency_name = models.CharField(max_length=256, blank=True, null=True)
  emergency_phone = models.CharField(max_length=20, blank=True, null=True)
  emergency_address_street_1 = models.CharField(max_length=128, blank=True, null=True)
  emergency_address_street_2 = models.CharField(max_length=128, blank=True, null=True)
  emergency_address_street_3 = models.CharField(max_length=128, blank=True, null=True)
  emergency_settlement = models.CharField(max_length=128, blank=True, null=True)
  emergency_locality = models.CharField(max_length=128, blank=True, null=True)
  emergency_postal_code = models.CharField(max_length=20, blank=True, null=True)
  emergency_country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.CASCADE, related_name="emergency_country_country")
  avatar = models.CharField(max_length=255, blank=True, null=True)
  dark_mode = models.BooleanField(default=False)
  comments = models.TextField(blank=True, null=True)
  first_password = models.BooleanField(default=True)
  pending_email = models.EmailField(max_length=255, blank=True, null=True)
  email_change_token = models.CharField(max_length=255, blank=True, null=True)
  email_change_token_date_created = models.DateTimeField(blank=True, null=True)
  events = models.ManyToManyField(Event, related_name="events")
  last_app_login = models.DateTimeField("Date Last Logged into App", blank=True, null=True)
  date_created = models.DateTimeField("Date Created", default=now, editable=False)
  date_updated = models.DateTimeField("Date Updated", auto_now=True, null=True)

  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = [
    'first_name',
    'last_name']

  def get_full_name(self):
    """
    Return the first_name plus the last_name, with a space in between.
    """
    full_name = '%s %s' % (
    self.first_name,
    self.last_name)
    return full_name.strip()

  def __str__(self):
    return '{} <{}>'.format(self.get_full_name(), self.email)
