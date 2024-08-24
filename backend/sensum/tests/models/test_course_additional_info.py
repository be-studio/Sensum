from django.test import TestCase
from ...models import CourseAdditionalInfo


class CourseAdditionalInfoTestCase(TestCase):
  @classmethod
  def setUpClass(cls):
    super().setUpClass()

    CourseAdditionalInfo.objects.create(
      title="Lorem Ipsum Dolor",
      description="This is a course."
    )

  def test_course_additional_info_created(self):
    info = CourseAdditionalInfo.objects.get(title="Lorem Ipsum Dolor")
    self.assertEqual(info.description, "This is a course.")

  def test_get_default_string(self):
    info = CourseAdditionalInfo.objects.get(title="Lorem Ipsum Dolor")
    self.assertEqual(info.__str__(), "Lorem Ipsum Dolor")
