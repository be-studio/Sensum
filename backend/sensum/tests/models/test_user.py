from django.contrib.auth import get_user_model
from ...models import UserPermission, UserGroup
from django.test import TestCase


class UserTestCase(TestCase):
  def setUp(self):
    user = get_user_model()
    UserPermission.objects.create(
      permission="test",
      alias="Test"
    )
    UserGroup.objects.create(
      group="group",
      alias="Group"
    )
    group = UserGroup.objects.get(group="group")
    group.permissions.add(UserPermission.objects.get(permission="test"))
    john = user.objects.create(
      first_name="John",
      last_name="Doe",
      email="john.doe@email.com",
    )
    john.user_groups.add(group)

  def test_user_created(self):
    user = get_user_model()
    john = user.objects.get(first_name="John")
    self.assertEqual(john.first_name, "John")
    self.assertEqual(john.last_name, "Doe")
    self.assertEqual(john.email, "john.doe@email.com")
    self.assertQuerySetEqual(
      john.user_groups.all(), [
        UserGroup.objects.get(group="group")]
    )

  def test_get_full_user_name(self):
    user = get_user_model()
    john = user.objects.get(first_name="John")
    self.assertEqual(john.get_full_name(), "John Doe")

  def test_get_default_string(self):
    user = get_user_model()
    john = user.objects.get(first_name="John")
    self.assertEqual(john.__str__(), "John Doe <john.doe@email.com>")
