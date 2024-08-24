from django.test import TestCase
from datetime import timedelta
from ...models import Course, Group, Lecturer, Sponsor, CourseAdditionalInfo


class CourseTestCase(TestCase):
  @classmethod
  def setUpClass(cls):
    super().setUpClass()

    audience_group = Group.objects.create(
      name="Visitors"
    )
    lecturer = Lecturer.objects.create(
      name="Jane Brown"
    )
    sponsor = Sponsor.objects.create(
      name="Toothpaste"
    )
    additional_info = CourseAdditionalInfo.objects.create(
      title="Extra",
      description="More Info"
    )
    course = Course.objects.create(
      title="Lorem Ipsum Dolor",
      primary_subtitle="Hello World",
      secondary_subtitle="Foo Bar",
      duration=timedelta(hours=1),
      about_description="This is a course for everyone",
      additional_info=additional_info
    )
    course.audience_groups.add(audience_group)
    course.lecturers.add(lecturer)
    course.sponsors.add(sponsor)

  def test_course_created(self):
    course = Course.objects.get(title="Lorem Ipsum Dolor")
    self.assertEqual(course.primary_subtitle, "Hello World")
    self.assertEqual(course.secondary_subtitle, "Foo Bar")
    self.assertEqual(course.duration, timedelta(hours=1))
    self.assertQuerySetEqual(course.audience_groups.all(), [Group.objects.get(name="Visitors")])
    self.assertQuerySetEqual(course.lecturers.all(), [Lecturer.objects.get(name="Jane Brown")])
    self.assertQuerySetEqual(course.sponsors.all(), [Sponsor.objects.get(name="Toothpaste")])
    self.assertEqual(course.about_description, "This is a course for everyone")
    self.assertEqual(course.additional_info, CourseAdditionalInfo.objects.get(title="Extra"))

  def test_get_default_string(self):
    course = Course.objects.get(title="Lorem Ipsum Dolor")
    self.assertEqual(course.__str__(), "Lorem Ipsum Dolor")
