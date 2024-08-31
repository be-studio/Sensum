from django.test import TestCase
from django.db import DataError, IntegrityError
from datetime import timedelta
from ...models import Course, Group, Lecturer, Sponsor, CourseAdditionalInfo
from ...utility.testing_utils import createRegex


class CourseTestCase(TestCase):
  @classmethod
  def setUpClass(cls):
    super().setUpClass()

    Group.objects.create(
      name="Visitors"
    )
    Lecturer.objects.create(
      name="Jane Brown"
    )
    Sponsor.objects.create(
      name="Toothpaste"
    )
    CourseAdditionalInfo.objects.create(
      title="Extra",
      description="More Info"
    )

  @staticmethod
  def create_course(title="Lorem Ipsum Dolor", primary_subtitle="Hello World", secondary_subtitle="Foo Bar"):
    audience_group = Group.objects.get(name="Visitors")
    lecturer = Lecturer.objects.get(name="Jane Brown")
    sponsor = Sponsor.objects.get(name="Toothpaste")
    additional_info = CourseAdditionalInfo.objects.get(title="Extra")

    course = Course.objects.create(
      title=title,
      primary_subtitle=primary_subtitle,
      secondary_subtitle=secondary_subtitle,
      duration=timedelta(hours=1),
      about_description="This is a course for everyone",
      additional_info=additional_info
    )
    course.audience_groups.add(audience_group)
    course.lecturers.add(lecturer)
    course.sponsors.add(sponsor)

    return course

  def test_course_created(self):
    course = self.create_course()

    self.assertEqual(course.primary_subtitle, "Hello World")
    self.assertEqual(course.secondary_subtitle, "Foo Bar")
    self.assertEqual(course.duration, timedelta(hours=1))
    self.assertQuerySetEqual(course.audience_groups.all(), [Group.objects.get(name="Visitors")])
    self.assertQuerySetEqual(course.lecturers.all(), [Lecturer.objects.get(name="Jane Brown")])
    self.assertQuerySetEqual(course.sponsors.all(), [Sponsor.objects.get(name="Toothpaste")])
    self.assertEqual(course.about_description, "This is a course for everyone")
    self.assertEqual(course.additional_info, CourseAdditionalInfo.objects.get(title="Extra"))

  def test_unique_course_title(self):
    with self.assertRaisesRegex(IntegrityError, createRegex("duplicate entry")):
      for _ in range(2):
        self.create_course()

  def test_valid_course_title_length(self):
    with self.assertRaisesRegex(DataError, createRegex("data too long")):
      self.create_course("x" * 121)

  def test_valid_course_primary_subtitle_length(self):
    with self.assertRaisesRegex(DataError, createRegex("data too long")):
      self.create_course(primary_subtitle="x" * 501)

  def test_valid_course_secondary_subtitle_length(self):
    with self.assertRaisesRegex(DataError, createRegex("data too long")):
      self.create_course(secondary_subtitle="x" * 501)

  def test_course_audience_groups_verbose_name(self):
    course = self.create_course()

    self.assertEqual(course._meta.get_field("audience_groups").verbose_name, "Audience Groups")

  def test_get_default_string(self):
    course = self.create_course()

    self.assertEqual(course.__str__(), "Lorem Ipsum Dolor")
