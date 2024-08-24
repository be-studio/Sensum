from django.test import TestCase
from datetime import time, date
from ...models import Event, Course


class EventTestCase(TestCase):
  @classmethod
  def setUpClass(cls):
    super().setUpClass()

    course = Course.objects.create(
      title="A Course"
    )
    event = Event.objects.create(
      title="Foo Bar",
      subtitle="Lorem Ipsum",
      time=time(12, 10),
      date=date(2024, 1, 2),
      location="Somewhere",
      course=course
    )

  def test_event_created(self):
    event = Event.objects.get(title="Foo Bar")
    self.assertEqual(event.subtitle, "Lorem Ipsum")
    self.assertEqual(event.time, time(12, 10))
    self.assertEqual(event.date, date(2024, 1, 2))
    self.assertEqual(event.location, "Somewhere")
    self.assertEqual(event.course, Course.objects.get(title="A Course"))

  def test_get_default_string(self):
    event = Event.objects.get(title="Foo Bar")
    self.assertEqual(event.__str__(), "Foo Bar")
