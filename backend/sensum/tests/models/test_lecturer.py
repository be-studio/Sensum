from django.test import TestCase
from ...models import Lecturer


class LecturerTestCase(TestCase):
  @classmethod
  def setUpClass(cls):
    super().setUpClass()

    Lecturer.objects.create(
      name="Jane Brown"
    )

  def test_lecturer_created(self):
    lecturer = Lecturer.objects.get(name="Jane Brown")
    self.assertEqual(lecturer.name, "Jane Brown")

  def test_get_default_string(self):
    lecturer = Lecturer.objects.get(name="Jane Brown")
    self.assertEqual(lecturer.__str__(), "Jane Brown")
