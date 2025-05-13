from rest_framework.routers import SimpleRouter
from api.events.views import EventViewSet

router = SimpleRouter()
router.register(r'', EventViewSet, basename='event')

urlpatterns = router.urls
