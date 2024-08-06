from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from ...serializers.refresh_jwt_serializer import RefreshJwtSerializer
from .refresh_jwt_set_cookie import set_cookie


class RefreshJwtView(TokenRefreshView):
  def finalize_response(self, request, response, *args, **kwargs):
    response = set_cookie(response)

    return super().finalize_response(request, response, *args, **kwargs)

  serializer_class = RefreshJwtSerializer
