from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model

from .serializers import (
    UserDetailSerializer,
    EnhancedUserSerializer,
    UserSummarySerializer,
    PrivateUserSerializer
)
from api.core.permissions import IsSelfOrReadOnly
from rest_framework import generics

User = get_user_model()


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSummarySerializer
    permission_classes = (AllowAny,)


class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsSelfOrReadOnly,)

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return EnhancedUserSerializer
        return UserDetailSerializer


class MeView(generics.RetrieveUpdateAPIView):
    serializer_class = PrivateUserSerializer

    def get_object(self):
        return self.request.user
