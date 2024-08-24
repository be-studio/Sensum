from django.test import TestCase
from django.db import DataError, IntegrityError
from datetime import time, date
from ...models import Event, Course
from ...utility.testing_utils import createRegex


class EventTestCase(TestCase):
  def setUp(self):
    Course.objects.create(
      title="A Course"
    )

  @staticmethod
  def create_event(title="Foo Bar", subtitle="Lorem Ipsum", location="Somewhere"):
    course = Course.objects.get(title="A Course")

    return Event.objects.create(
      title=title,
      subtitle=subtitle,
      time=time(12, 10),
      date=date(2024, 1, 2),
      location=location,
      course=course
    )

  def test_event_created(self):
    event = self.create_event()

    self.assertEqual(event.title, "Foo Bar")
    self.assertEqual(event.subtitle, "Lorem Ipsum")
    self.assertEqual(event.time, time(12, 10))
    self.assertEqual(event.date, date(2024, 1, 2))
    self.assertEqual(event.location, "Somewhere")
    self.assertEqual(event.course, Course.objects.get(title="A Course"))

  def test_unique_event_title(self):
    with self.assertRaisesRegex(DataError, createRegex("data too long")):
      self.create_event("x" * 61)

  def test_unique_event_subtitle(self):
    with self.assertRaisesRegex(DataError, createRegex("data too long")):
      self.create_event(subtitle="x" * 121)

  def test_unique_location_title(self):
    with self.assertRaisesRegex(DataError, createRegex("data too long")):
      self.create_event(location="x" * 91)

  def test_get_default_string(self):
    event = self.create_event(title="Foo Bar")

    self.assertEqual(event.__str__(), "Foo Bar")
