from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views.sample import SampleView
from api.views.auth.create_token import AuthCreateTokenView
from api.views.auth.refresh_token import AuthRefreshTokenView
from api.views.auth.verify_token import AuthVerifyTokenView
from api.views.auth.blacklist import AuthBlacklistView

# ViewSetを使ってない場合はこっち
urlpatterns = [
    path('auth/token/create', AuthCreateTokenView.as_view(), name='auth-token-create'),
    path('auth/token/refresh', AuthRefreshTokenView.as_view(), name='auth-token-refresh'),
    path('auth/token/verify', AuthVerifyTokenView.as_view(), name='auth-token-verify'),
    path('auth/token/blacklist', AuthBlacklistView.as_view(), name='auth-token-blacklist'),
]

# ViewSetを使ってる場合はこっち
router = DefaultRouter(trailing_slash=False)
router.register(prefix='sample', viewset=SampleView, basename='sample')

urlpatterns += router.urls
