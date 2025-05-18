from rest_framework.routers import SimpleRouter
from api.core.views import CountryViewSet, CityViewSet
from api.events.views import EventViewSet


router = SimpleRouter()

router.register(r'countries', CountryViewSet, basename='country')
router.register(r'cities', CityViewSet, basename='city')
router.register(r'events', EventViewSet, basename='event')

urlpatterns = router.urls
