from django.urls import path, include

from .views.auth import *

urlpatterns = [
  path("login", LoginView.as_view(), name="login"),
  path("get-csrf", get_csrf_view)
]
