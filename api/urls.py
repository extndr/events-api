from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from api.core.views import CountryViewSet, CityViewSet
from api.events.views import EventViewSet, AttendeeViewSet


router = DefaultRouter()

# core
router.register(r'countries', CountryViewSet, basename='country')
router.register(r'cities', CityViewSet, basename='city')

# events
router.register(r'events', EventViewSet, basename='event')
router.register(r'attendees', AttendeeViewSet, basename='attendee')

urlpatterns = [
    path('', include(router.urls)),

    path('jwt/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('accounts/', include('api.accounts.urls')),
]
