from rest_framework.routers import DefaultRouter
from api.views.sample import SampleView

router = DefaultRouter(trailing_slash=False)
router.register(prefix='sample', viewset=SampleView, basename='sample')

urlpatterns = router.urls
