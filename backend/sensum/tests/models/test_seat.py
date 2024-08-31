from django.contrib.auth import get_user_model
from django.test import TestCase
from django.db import DataError, IntegrityError
from ...models import Seat, Event
from ...utility.testing_utils import createRegex
from datetime import time, date


class SeatTestCase(TestCase):
  def setUp(self):
    user = get_user_model()

    user.objects.create(
      first_name="John",
      last_name="Doe",
      email="john.doe@email.com"
    )

    Event.objects.create(
      title="Foo Bar",
      time=time(12, 10),
      date=date(2024, 1, 2)
    )

  @staticmethod
  def create_seat(registration_number="12345"):
    user = get_user_model().objects.get(first_name="John")
    event = Event.objects.get(title="Foo Bar")

    return Seat.objects.create(
      user=user,
      registration_number=registration_number,
      event=event
    )

  def test_seat_created(self):
    seat = self.create_seat()

    user = get_user_model()

    self.assertEqual(seat.user, user.objects.get(first_name="John"))
    self.assertEqual(seat.registration_number, "12345")
    self.assertEqual(seat.event, Event.objects.get(title="Foo Bar"))

  def test_unique_seat_registration_number(self):
    with self.assertRaisesRegex(IntegrityError, createRegex("duplicate entry")):
      for _ in range(2):
        self.create_seat()

  def test_valid_seat_registration_number_length(self):
    with self.assertRaisesRegex(DataError, createRegex("data too long")):
      self.create_seat("x" * 61)

  def test_get_default_string(self):
    seat = self.create_seat();

    self.assertEqual(seat.__str__(), "John Doe")
