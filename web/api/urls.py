from rest_framework.routers import DefaultRouter
from api.views.sample import SampleView

router = DefaultRouter()
router.register('sample', SampleView, basename='sample')

urlpatterns = router.urls
