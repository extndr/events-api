from django.urls import path
from .views import UserListView, UserDetailView, MeView

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('me/', MeView.as_view(), name='me'),
]
