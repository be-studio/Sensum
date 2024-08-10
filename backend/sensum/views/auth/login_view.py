from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from ...utility.cookie_utils import set_cookie


class LoginView(TokenObtainPairView):
  def finalize_response(self, request, response, *args, **kwargs):
    response = set_cookie(response)

    return super().finalize_response(request, response, *args, **kwargs)
