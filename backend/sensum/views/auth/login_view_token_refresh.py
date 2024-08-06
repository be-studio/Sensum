from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from ...serializers.cookie_token_refresh_serializer import CookieTokenRefreshSerializer

class CookieTokenRefreshView(TokenRefreshView):
  def finalize_response(self, request, response, *args, **kwargs):
    if response.data.get('refresh'):
      cookie_max_age = 3600 * 24 * 14 # 14 days
      response.set_cookie('refresh_token', response.data['refresh'], max_age=cookie_max_age, httponly=True, samesite='none' )
      del response.data['refresh']
    return super().finalize_response(request, response, *args, **kwargs)
  serializer_class = CookieTokenRefreshSerializer
