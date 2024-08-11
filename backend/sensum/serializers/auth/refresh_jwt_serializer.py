from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.exceptions import InvalidToken


class RefreshJwtSerializer(TokenRefreshSerializer):
  refresh = None

  def validate(self, attrs):
    attrs['refresh'] = self.context['request'].COOKIES.get('refresh_token')

    if attrs['refresh']:
      return super().validate(attrs)
    else:
      raise InvalidToken("No valid refresh token has been found. Unable to continue.")
