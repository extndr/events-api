from django.urls import path, include
from rest_framework.routers import SimpleRouter
from api.accounts.views import RegisterView, UserViewSet, ProfileViewSet

router = SimpleRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'profiles', ProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
]
