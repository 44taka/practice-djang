from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views.sample import SampleView

router = DefaultRouter()
router.register('api', SampleView, basename='api')

urlpatterns = router.urls

# urlpatterns = [
#     # path('api/', SampleView.as_view(), name="api"),
#     # path('api/', SampleView.as_view({'get': 'list'}), name="api"),
#     path('api/', SampleView.as_view({'get': 'list'}), name="api"),
# ]