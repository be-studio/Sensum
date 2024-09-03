from django.db import DataError
from django.test import TestCase
from datetime import time, date
from decimal import Decimal
from ...utility.testing_utils import createRegex
from ...models import Offer, Event


class OfferTestCase(TestCase):
  def setUp(self):
    Event.objects.create(
      title="Foo Bar",
      time=time(12, 10),
      date=date(2024, 1, 2)
    )

  def test_offer_created(self):
    event = Event.objects.get(title="Foo Bar")
    Offer.objects.create(
      id=100,
      price=Decimal('100.99'),
      description="Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.",
      event=event
    )

    offer = Offer.objects.get(id=100)
    self.assertEqual(offer.price, Decimal('100.99'))
    self.assertEqual(offer.description, "Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.")
    self.assertEqual(offer.event, Event.objects.get(title="Foo Bar"))

  def test_default_price(self):
    event = Event.objects.get(title="Foo Bar")
    Offer.objects.create(
      id=100,
      description="Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.",
      event=event
    )

    offer = Offer.objects.get(id=100)
    self.assertEqual(offer.price, 0)

  def test_valid_price(self):
    with self.assertRaisesRegex(DataError, createRegex("out of range")):
      event = Event.objects.get(title="Foo Bar")
      Offer.objects.create(
        id=100,
        price=Decimal('100000.99'),
        description="Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.",
        event=event
      )

  def test_get_default_string(self):
    event = Event.objects.get(title="Foo Bar")
    Offer.objects.create(
      id=100,
      price=Decimal('100.99'),
      description="Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.",
      event=event
    )

    offer = Offer.objects.get(id=100)
    self.assertEqual(offer.__str__(), "100.99 - Vivamus sagittis lac...")
