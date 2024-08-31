from django.conf import settings
from typing import Literal


def set_cookie(response):
  if response.data.get("refresh"):
    response = _handle_cookie_on_response(response, "set")

    del response.data["refresh"]

  return response


def remove_cookie(response):
  response = _handle_cookie_on_response(response, "remove")

  return response


def _handle_cookie_on_response(response, kind: Literal["set", "remove"]):
  set_args = {
    "key": settings.SIMPLE_JWT["AUTH_COOKIE"],
    "value": response.data["refresh"] if kind == "set" else "",
    "secure": settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
    "httponly": settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
    "samesite": settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"]
  }

  if kind == "set":
    set_args["max_age"] = settings.SIMPLE_JWT["REFRESH_TOKEN_MAX_AGE"]

  if kind == "remove":
    set_args["expires"] = 1

  response.set_cookie(**set_args)

  return response
