from rest_framework.routers import SimpleRouter
from api.users.views import ProfileViewSet, UserViewSet
from api.core.views import CountryViewSet, CityViewSet
from api.events.views import EventViewSet


router = SimpleRouter()

router.register(r'countries', CountryViewSet, basename='country')
router.register(r'cities', CityViewSet, basename='city')
router.register(r'events', EventViewSet, basename='event')
router.register(r'users', UserViewSet, basename='user')
router.register(r'profiles', ProfileViewSet, basename='profile')

urlpatterns = router.urls
