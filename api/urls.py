from django.urls import path, include
from django.contrib.admin.views.decorators import staff_member_required
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

    # API docs (only for admins)
    path('schema/', staff_member_required(SpectacularAPIView.as_view()), name='schema'),
    path('docs/', staff_member_required(SpectacularSwaggerView.as_view(url_name='schema')), name='swagger-ui'),
    path('docs/redoc/', staff_member_required(SpectacularRedocView.as_view(url_name='schema')), name='redoc'),
]
