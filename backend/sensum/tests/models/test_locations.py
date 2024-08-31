from django.test import TestCase
from django.db import DataError, IntegrityError
from ...models import Country, Department
from ...utility.testing_utils import createRegex


class CountryTestCase(TestCase):
  @staticmethod
  def create_country(country="State", alt_name="Republic of State", iso_code="STATE"):
    return Country.objects.create(
      country=country,
      alt_name=alt_name,
      iso_code=iso_code
    )

  def test_country_created(self):
    country = self.create_country()

    self.assertEqual(country.country, "State")
    self.assertEqual(country.alt_name, "Republic of State")
    self.assertEqual(country.iso_code, "STATE")

  def test_unique_country_name(self):
    with self.assertRaisesRegex(IntegrityError, createRegex("duplicate entry")):
      for _ in range(2):
        self.create_country()

  def test_valid_country_name_length(self):
    with self.assertRaisesRegex(DataError, createRegex("data too long")):
      self.create_country("x" * 129)

  def test_valid_country_alt_name_length(self):
    with self.assertRaisesRegex(DataError, createRegex("data too long")):
      self.create_country(alt_name="x" * 129)

  def test_valid_iso_code_length(self):
    with self.assertRaisesRegex(DataError, createRegex("data too long")):
      self.create_country(iso_code="SOMEOTHERSTATE")


class DepartmentTestCase(TestCase):
  @staticmethod
  def create_department(department="Place"):
    return Department.objects.create(
      department=department,
      description="Somewhere to go"
    )

  def test_department_created(self):
    department = self.create_department()

    self.assertEqual(department.department, "Place")
    self.assertEqual(department.description, "Somewhere to go")

  def test_unique_department_name(self):
    with self.assertRaisesRegex(IntegrityError, createRegex("duplicate entry")):
      for _ in range(2):
        self.create_department()

  def test_valid_department_name_length(self):
    with self.assertRaisesRegex(DataError, createRegex("data too long")):
      self.create_department("x" * 129)
