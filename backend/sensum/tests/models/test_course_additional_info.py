from django.test import TestCase
from django.db import DataError
from ...models import CourseAdditionalInfo
from ...utility.testing_utils import createRegex


class CourseAdditionalInfoTestCase(TestCase):
  @staticmethod
  def create_course_additional_info(title="Lorem Ipsum Dolor"):
    return CourseAdditionalInfo.objects.create(
      title=title,
      description="This is a course."
    )

  def test_course_additional_info_created(self):
    info = self.create_course_additional_info()

    self.assertEqual(info.title, "Lorem Ipsum Dolor")
    self.assertEqual(info.description, "This is a course.")

  def test_valid_course_additional_info_title_length(self):
    with self.assertRaisesRegex(DataError, createRegex("data too long")):
      self.create_course_additional_info("x" * 121)

  def test_get_default_string(self):
    info = self.create_course_additional_info()

    self.assertEqual(info.__str__(), "Lorem Ipsum Dolor")
