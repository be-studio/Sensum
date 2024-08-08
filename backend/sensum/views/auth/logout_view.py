from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenVerifyView

class LogoutView(APIView):
  permission_classes = (IsAuthenticated,)

  def post(self, request):
    try:
      refresh_token = request.COOKIES.get("refresh_token")
      token = RefreshToken(refresh_token)
      token.blacklist()

      logout(request)

      response = Response(status=status.HTTP_205_RESET_CONTENT)

      return response
    except Exception as e:
      return Response(status=status.HTTP_400_BAD_REQUEST)
