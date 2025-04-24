from rest_framework.routers import DefaultRouter
from api.events.views import CountryViewSet, CityViewSet, EventViewSet

router = DefaultRouter()

router.register(r'countries', CountryViewSet, basename='country')
router.register(r'cities', CityViewSet, basename='city')
router.register(r'events', EventViewSet, basename='event')

urlpatterns = router.urls
