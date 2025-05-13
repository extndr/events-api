from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from api.core.views import CountryViewSet, CityViewSet
from api.events.views import EventViewSet
from api.accounts.views import ProfileViewSet, UserViewSet, RegisterView


router = DefaultRouter()

# core
router.register(r'countries', CountryViewSet, basename='country')
router.register(r'cities', CityViewSet, basename='city')

# events
router.register(r'events', EventViewSet, basename='event')

# accounts
router.register(r'users', UserViewSet, basename='user')
router.register(r'profiles', ProfileViewSet, basename='profile')


urlpatterns = [
    path('', include(router.urls)),

    path('register/', RegisterView.as_view(), name='register'),

    path('jwt/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
