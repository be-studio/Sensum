from django.test import TestCase
from django.db import DataError, IntegrityError
from ...models import Sponsor
from ...utility.testing_utils import createRegex


class SponsorTestCase(TestCase):
  @staticmethod
  def create_sponsor(name="Toothpaste", logo="path.to/file", link="https://www.www.com"):
    return Sponsor.objects.create(
      name=name,
      logo=logo,
      link=link
    )

  def test_sponsor_created(self):
    sponsor = self.create_sponsor()

    self.assertEqual(sponsor.name, "Toothpaste")
    self.assertEqual(sponsor.logo, "path.to/file")
    self.assertEqual(sponsor.link, "https://www.www.com")

  def test_unique_sponsor_name(self):
    with self.assertRaisesRegex(IntegrityError, createRegex("duplicate entry")):
      for _ in range(2):
        self.create_sponsor()

  def test_valid_sponsor_name_length(self):
    with self.assertRaisesRegex(DataError, createRegex("data too long")):
      self.create_sponsor("x" * 31)

  def test_valid_sponsor_logo_length(self):
    with self.assertRaisesRegex(DataError, createRegex("data too long")):
      self.create_sponsor(logo="x" * 301)

  def test_valid_sponsor_link_length(self):
    with self.assertRaisesRegex(DataError, createRegex("data too long")):
      self.create_sponsor(link="x" * 301)

  def test_get_default_string(self):
    sponsor = self.create_sponsor()

    self.assertEqual(sponsor.__str__(), "Toothpaste")
