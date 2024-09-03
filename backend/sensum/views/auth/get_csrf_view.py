from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_csrf_view() -> JsonResponse:
  """Gets a CSRF token for subsequent HTTP requests by the client.

  :return:
  :rtype: JsonResponse
  """
  return JsonResponse({})
