from django.test import TestCase
from django.db import DataError
from ...models import Country, Department
from ...utility.testing_utils import createRegex


class CountryTestCase(TestCase):
  def test_country_created(self):
    Country.objects.create(
      country="State",
      alt_name="Republic of State",
      iso_code="STATE"
    )

    country = Country.objects.get(country="State")
    self.assertEqual(country.alt_name, "Republic of State")
    self.assertEqual(country.iso_code, "STATE")

  def test_invalid_country_name_length(self):
    with self.assertRaisesRegex(DataError, createRegex("data too long")):
      Country.objects.create(
        country="x" * 129,
        alt_name="Republic of State",
        iso_code="STATE"
      )

  def test_invalid_country_alt_name_length(self):
    with self.assertRaisesRegex(DataError, createRegex("data too long")):
      Country.objects.create(
        country="State",
        alt_name="x" * 129,
        iso_code="STATE"
      )

  def test_invalid_iso_code_length(self):
    with self.assertRaisesRegex(DataError, createRegex("data too long")):
      Country.objects.create(
        country="Country",
        alt_name="Republic of State",
        iso_code="SOMEOTHERSTATE"
      )


class DepartmentTestCase(TestCase):
  def test_department_created(self):
    Department.objects.create(
      department="Place",
      description="Somewhere to go"
    )

    department = Department.objects.get(department="Place")
    self.assertEqual(department.description, "Somewhere to go")

  def test_invalid_department_name_length(self):
    with self.assertRaisesRegex(DataError, createRegex("data too long")):
      Department.objects.create(
        department="x" * 129,
        description="Somewhere to go"
      )
