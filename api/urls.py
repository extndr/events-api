from django.urls import path, include
from django.conf import settings
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

from api.routes import urlpatterns as router_urls

urlpatterns = [
    path('', include(router_urls)),
    path('accounts/', include('api.accounts.urls')),
    path('users/', include('api.users.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path('schema/', SpectacularAPIView.as_view(), name='schema'),
        path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]
