from django.urls import path
from api.views.sample import SampleView
from api.views.user_info import UserInfoView
from api.views.user_info_detail import UserInfoDetailView

urlpatterns = [
    path('api/', SampleView.as_view(), name="api"),
    path('api/userinfo/', UserInfoView.as_view(), name="api/userinfo/"),
    path('api/userinfo/<int:pk>', UserInfoDetailView.as_view(), name="api/userinfo/")
]
