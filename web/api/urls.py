from django.urls import path
from . import apis

urlpatterns = [
    path('api/', apis.Api.as_view(), name="api")
]