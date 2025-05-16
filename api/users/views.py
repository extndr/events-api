from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response

from api.core.permissions import IsSelfOrReadOnly

from .serializers import UserSerializer, ProfileSerializer
from .models import Profile
from .filters import ProfileFilter
from .services import ProfileService


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    filterset_fields = ('username', 'email', 'is_staff', 'is_active')


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filterset_class = ProfileFilter

    @action(
        detail=False,
        methods=['get', 'patch'],
        permission_classes=[IsAuthenticated & IsSelfOrReadOnly],
        url_path='me'
    )
    def me(self, request):
        profile = ProfileService.get_profile(request.user)

        if request.method == 'GET':
            serializer = self.get_serializer(profile)
            return Response(serializer.data)

        serializer = self.get_serializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        updated_profile = ProfileService.update_profile(profile, serializer.validated_data)
        response_serializer = self.get_serializer(updated_profile)
        return Response(response_serializer.data)
