from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .refresh_jwt_set_cookie import set_cookie


class LoginView(TokenObtainPairView):
  def finalize_response(self, request, response, *args, **kwargs):
    response = set_cookie(response)

    return super().finalize_response(request, response, *args, **kwargs)
