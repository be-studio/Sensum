from django.test import TestCase
from django.db import DataError, IntegrityError
from ...models import Lecturer
from ...utility.testing_utils import createRegex


class LecturerTestCase(TestCase):
  def test_lecturer_created(self):
    lecturer = Lecturer.objects.create(
      name="Jane Brown"
    )

    self.assertEqual(lecturer.name, "Jane Brown")

  def test_unique_lecturer_name(self):
    with self.assertRaisesRegex(IntegrityError, createRegex("duplicate entry")):
      for _ in range(2):
        Lecturer.objects.create(
          name="Jane Brown"
        )

  def test_valid_lecturer_name_length(self):
    with self.assertRaisesRegex(DataError, createRegex("data too long")):
      Lecturer.objects.create(
        name="x" * 61
      )

  def test_get_default_string(self):
    lecturer = Lecturer.objects.create(
      name="Jane Brown"
    )

    self.assertEqual(lecturer.__str__(), "Jane Brown")
