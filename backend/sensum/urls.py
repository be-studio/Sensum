from django.urls import path, include
from rest_framework_simplejwt.views import TokenVerifyView

from .views.auth import *
from .views.user import *

urlpatterns = [
  path("get-csrf", get_csrf_view, name="get_csrf"),
  path("login", LoginView.as_view(), name="login"),
  path("logout", LogoutView.as_view(), name="logout"),
  path("verify-jwt", TokenVerifyView.as_view(), name="verify_jwt"),
  path("refresh-jwt", RefreshJwtView.as_view(), name="refresh_jwt"),
  path("users", UsersView.as_view(), name="users")
]
