from django.urls import path
from api.views.sample import SampleView


urlpatterns = [
    path('api/', SampleView.as_view(), name="api")
]
