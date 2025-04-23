from rest_framework.routers import DefaultRouter
from api.events.views import EventViewSet

router = DefaultRouter()

router.register(r'events', EventViewSet, basename='event')

urlpatterns = router.urls
