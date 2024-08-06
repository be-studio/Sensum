from django.urls import path, include

from .views.auth import *
from .views.user import *

urlpatterns = [
  path("login", LoginView.as_view(), name="login"),
  path("get-csrf", get_csrf_view),
  path("jwt-refresh", JwtRefreshView.as_view(), name="token_refresh"),

  path("login-alt", CookieTokenObtainPairView.as_view()),
  path("refresh-alt", CookieTokenRefreshView.as_view()),
  path("users", UsersView.as_view(), name="users")
]
