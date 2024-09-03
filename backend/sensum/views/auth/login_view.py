from rest_framework_simplejwt.views import TokenObtainPairView
from ...serializers.auth.log_user_app_login_serializer import LogUserAppLoginSerializer
from ...utility.cookie_utils import set_cookie


class LoginView(TokenObtainPairView):
  serializer_class = LogUserAppLoginSerializer

  def finalize_response(self, request, response, *args, **kwargs):
    response = set_cookie(response)

    return super().finalize_response(request, response, *args, **kwargs)
