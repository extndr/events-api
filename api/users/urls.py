from email.mime import base
from rest_framework.routers import SimpleRouter
from api.users.views import UserViewSet, ProfileViewSet

router = SimpleRouter()
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'', UserViewSet, basename='user')

urlpatterns = router.urls
