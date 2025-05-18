from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSelfOrReadOnly(BasePermission):
    """
    Allows read-only access to any user.
    Write permissions are only granted to the owner of the object.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            obj == request.user
        )


class IsAdminOrReadOnly(BasePermission):
    """
    Allows read-only access to any user.
    Write permissions are only granted to admin users.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and request.user.is_staff
        )
