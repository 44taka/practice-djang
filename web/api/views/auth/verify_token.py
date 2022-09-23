from rest_framework_simplejwt.views import TokenVerifyView
from api.serializers.auth.verify_token import TokenVerifySerializer


class AuthVerifyTokenView(TokenVerifyView):
    serializer_class = TokenVerifySerializer
