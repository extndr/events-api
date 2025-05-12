from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from api.core.permissions import IsSelfOrReadOnly
from .serializers import UserRegisterSerializer, ProfileSerializer
from .models import Profile


class RegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Response({
            "message": "User created successfully",
            "access": access_token,
            "refresh": refresh_token,
        }, status=status.HTTP_201_CREATED)


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAdminUser, IsSelfOrReadOnly)
