from django.conf import settings


def set_cookie(response):
  if response.data.get('refresh'):
    response.set_cookie(
      key = settings.SIMPLE_JWT['AUTH_COOKIE'],
      value=response.data['refresh'],
      expires = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
      secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
      httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
      samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
    )

    del response.data['refresh']

  return response
