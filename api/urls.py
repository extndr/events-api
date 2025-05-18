from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

from api.routes import urlpatterns as router_urls

urlpatterns = [
    # API modules
    path('', include(router_urls)),
    path('accounts/', include('api.accounts.urls')),
    path('users/', include('api.users.urls')),

    # API docs
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
