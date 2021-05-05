from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class IsProjectOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permission.SAFE_METHODS:
            return True
        return obj.owner == request.obj
