from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.contrib.auth import authenticate, login
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.conf import settings

from rest_framework_simplejwt.tokens import RefreshToken

import json

class LoginView(View):
  def get_tokens_for_user(self, user):
    refresh = RefreshToken.for_user(user)

    return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
    }

  @method_decorator(ensure_csrf_cookie)
  def post(self, request):
    """Handles login request from the client..

    :param request:
    :type request: HttpRequest
    :return:
    :rtype: HttpResponse or HttpResponseForbidden
    """
    # Need to decode the request body, which is of the form bytestring.
    body_unicode: object = request.body.decode("utf-8")
    body = json.loads(body_unicode)


    user = authenticate(
      username=body["username"],
      password=body["password"]
    )

    if user is not None:
      login(request, user)
      tokens = self.get_tokens_for_user(user)
      response = JsonResponse(tokens["access"], status=200, safe=False)
      response.set_cookie(key = settings.SIMPLE_JWT['AUTH_COOKIE'],
        value = self.get_tokens_for_user(user)["refresh"],
        expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
        secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
        httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
        samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'])
      return response
    else:
      return HttpResponse(status=403)

