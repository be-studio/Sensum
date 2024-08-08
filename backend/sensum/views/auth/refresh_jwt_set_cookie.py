from django.conf import settings


def set_cookie(response):
  if response.data.get('refresh'):
    response.set_cookie(
      key = settings.SIMPLE_JWT['AUTH_COOKIE'],
      value=response.data['refresh'],
      max_age = 60 * 60 * 24 * 7,
      secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
      httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
      samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
    )

    del response.data['refresh']

  return response
