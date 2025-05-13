from rest_framework.routers import SimpleRouter
from api.core.views import CountryViewSet, CityViewSet

router = SimpleRouter()
router.register(r'countries', CountryViewSet, basename='country')
router.register(r'cities', CityViewSet, basename='city')

urlpatterns = router.urls
