from rest_framework.permissions import BasePermission

class IsLibraryStockOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.groups.filter(name='library').exists():
                return obj.library == request.user.library
        return False