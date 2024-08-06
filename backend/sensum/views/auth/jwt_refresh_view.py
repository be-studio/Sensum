from rest_framework import authentication
from rest_framework import permissions

from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken

class JwtRefreshView(TokenRefreshView):


  # Need to override the blank tuple values of the following that are present in
  # `TokenRefreshView` to ensure secure token refresh access.
  permission_classes = (permissions.IsAuthenticated,)
  authentication_classes = (authentication.SessionAuthentication,)
