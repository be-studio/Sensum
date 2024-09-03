from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.settings import api_settings
from datetime import datetime


class LogUserAppLoginSerializer(TokenObtainPairSerializer):
  def validate(self, attrs):
    data = super().validate(attrs)

    refresh = self.get_token(self.user)

    data["refresh"] = str(refresh)
    data["access"] = str(refresh.access_token)

    self.user.last_app_login = datetime.now()
    self.user.save()

    if api_settings.UPDATE_LAST_LOGIN:
      update_last_login(None, self.user)

    return data
