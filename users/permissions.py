from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminRole(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        if user.is_superuser or user.is_staff:
            return True
        role = getattr(user, 'role', None)
        return bool(role and role.name == 'administrador')


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return IsAdminRole().has_permission(request, view)


class IsAdminOrCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return IsAdminRole().has_permission(request, view)
