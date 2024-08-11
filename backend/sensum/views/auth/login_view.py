from django.contrib.auth import \
  get_user_model
from rest_framework import \
  status
from rest_framework.response import \
  Response
from rest_framework_simplejwt.exceptions import \
  TokenError, \
  InvalidToken
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from ...serializers.auth.log_user_app_login_serializer import LogUserAppLoginSerializer
from ...utility.cookie_utils import set_cookie
import datetime


class LoginView(TokenObtainPairView):
  serializer_class = LogUserAppLoginSerializer

  def finalize_response(self, request, response, *args, **kwargs):
    response = set_cookie(response)

    return super().finalize_response(request, response, *args, **kwargs)
