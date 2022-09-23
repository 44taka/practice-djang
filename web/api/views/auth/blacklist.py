from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework_simplejwt.exceptions import TokenError


class AuthBlacklistView(APIView):

    def post(self, request):
        try:
            token = RefreshToken(request.data.get('refresh'))
            token.blacklist()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except BlacklistedToken.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        except TokenError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e.with_traceback())
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
