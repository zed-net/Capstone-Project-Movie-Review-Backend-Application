from rest_framework import permissions

class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission: only owners or admins can edit/delete.
    Everyone can read.
    """

    def has_object_permission(self, request, view, obj):
        # Read-only permissions for safe methods (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions allowed if user is owner or is admin
        return obj.user == request.user or request.user.is_staff


class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    """
    Only owners and admins can update/delete.
    Authenticated users can read.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any authenticated request
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated

        # Write permissions only for owner or admin
        return obj.owner == request.user or request.user.is_staff