from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from django.test import Client, TestCase


class UserApiTestCase(TestCase):
  @classmethod
  def setUpClass(cls):
    super().setUpClass()

    user = get_user_model()
    user.objects.create(
      first_name="John",
      last_name="Doe",
      email="john.doe@email.com"
    )
    user.objects.create(
      first_name="Jane",
      last_name="Brown",
      email="jane.brown@email.com"
    )

  def test_get_users(self):
    user = get_user_model()
    c = Client()
    c.force_login(user=user.objects.get(first_name="John"))
    response = c.get("/users")

    self.assertEqual(
      response.json(), [
        {
          "first_name": "John",
          "last_name": "Doe",
          "email": "john.doe@email.com"
        },
        {
          "first_name": "Jane",
          "last_name": "Brown",
          "email": "jane.brown@email.com"
        }
      ]
    )

  def test_get_user(self):
    user = get_user_model()
    c = APIClient()
    c.force_authenticate(user=user.objects.get(first_name="John"))
    response = c.get("/api/user/1")

    self.assertEqual(
      response.json(), {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@email.com"
      }
    )
