from django.http import HttpResponse, HttpRequest, JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from typing import Union


class UsersView(APIView):
  permission_classes = (IsAuthenticated,)


  def get(self, request) -> Union[HttpResponse, JsonResponse]:
    try:
      User = get_user_model()
      users = list(User.objects.all().values(
        "first_name",
        "last_name",
        "email"
      ))
    except Exception:
      return HttpResponse(status=404)

    return JsonResponse(users, safe=False, status=200)
