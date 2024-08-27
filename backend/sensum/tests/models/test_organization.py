from django.test import TestCase
from django.db import DataError, IntegrityError
from ...models import Organization, Country
from ...utility.testing_utils import createRegex


class OrganizationTestCase(TestCase):
  error_too_long = createRegex("data too long")

  @classmethod
  def setUpClass(cls):
    super().setUpClass()

    Country.objects.create(
      country="State",
      alt_name="Republic of State",
      iso_code="STATE"
    )

  @staticmethod
  def create_organization(
    name="ACME Industries",
    avatar="path.to/file",
    email="name@email.com",
    address_street_1="The Building",
    address_street_2="The Street",
    address_street_3="1 The Square",
    settlement="Somewhere",
    locality="Someplace",
    postal_code="POST CODE",
    website="https://www.www.com",
    landline_phone="0123456789",
    extension="1234",
    mobile_phone="9876543"
  ):
    country = Country.objects.get(country="State")

    return Organization.objects.create(
      name=name,
      avatar=avatar,
      email=email,
      address_street_1=address_street_1,
      address_street_2=address_street_2,
      address_street_3=address_street_3,
      settlement=settlement,
      locality=locality,
      postal_code=postal_code,
      country=country,
      website=website,
      landline_phone=landline_phone,
      extension=extension,
      mobile_phone=mobile_phone
    )

  def test_organization_created(self):
    organization = self.create_organization()

    self.assertEqual(organization.name, "ACME Industries")
    self.assertEqual(organization.avatar, "path.to/file")
    self.assertEqual(organization.email, "name@email.com")
    self.assertEqual(organization.address_street_1, "The Building")
    self.assertEqual(organization.address_street_2, "The Street")
    self.assertEqual(organization.address_street_3, "1 The Square")
    self.assertEqual(organization.settlement, "Somewhere")
    self.assertEqual(organization.locality, "Someplace")
    self.assertEqual(organization.postal_code, "POST CODE")
    self.assertEqual(organization.country, Country.objects.get(country="State"))
    self.assertEqual(organization.website, "https://www.www.com")
    self.assertEqual(organization.landline_phone, "0123456789")
    self.assertEqual(organization.extension, "1234")
    self.assertEqual(organization.mobile_phone, "9876543")

  def test_unique_organization_name(self):
    with self.assertRaisesRegex(IntegrityError, createRegex("duplicate entry")):
      for _ in range(2):
        self.create_organization()

  def test_valid_organization_name_length(self):
    with self.assertRaisesRegex(DataError, self.error_too_long):
      self.create_organization("x" * 129)

  def test_valid_orgzanization_avatar_length(self):
    with self.assertRaisesRegex(DataError, self.error_too_long):
      self.create_organization(avatar="x" * 513)

  def test_valid_orgzanization_email_length(self):
    with self.assertRaisesRegex(DataError, self.error_too_long):
      self.create_organization(email="x" * 256)

  def test_valid_orgzanization_address_street_1_length(self):
    with self.assertRaisesRegex(DataError, self.error_too_long):
      self.create_organization(address_street_1="x" * 129)

  def test_valid_orgzanization_address_street_2_length(self):
    with self.assertRaisesRegex(DataError, self.error_too_long):
      self.create_organization(address_street_2="x" * 129)

  def test_valid_orgzanization_address_street_3_length(self):
    with self.assertRaisesRegex(DataError, self.error_too_long):
      self.create_organization(address_street_3="x" * 129)

  def test_valid_orgzanization_settlement_length(self):
    with self.assertRaisesRegex(DataError, self.error_too_long):
      self.create_organization(settlement="x" * 129)

  def test_valid_orgzanization_locality_length(self):
    with self.assertRaisesRegex(DataError, self.error_too_long):
      self.create_organization(locality="x" * 129)

  def test_valid_orgzanization_postal_code_length(self):
    with self.assertRaisesRegex(DataError, self.error_too_long):
      self.create_organization(postal_code="x" * 129)

  def test_organization_country_related_name(self):
    organization = self.create_organization()

    self.assertEqual(organization._meta.get_field("country")._related_name, "country_country")

  def test_valid_orgzanization_website_length(self):
    with self.assertRaisesRegex(DataError, self.error_too_long):
      self.create_organization(website="x" * 256)

  def test_valid_orgzanization_landline_phone_length(self):
    with self.assertRaisesRegex(DataError, self.error_too_long):
      self.create_organization(landline_phone="x" * 21)

  def test_valid_orgzanization_extension_length(self):
    with self.assertRaisesRegex(DataError, self.error_too_long):
      self.create_organization(extension="123456789")

  def test_valid_orgzanization_mobile_phone_length(self):
    with self.assertRaisesRegex(DataError, self.error_too_long):
      self.create_organization(mobile_phone="x" * 21)
