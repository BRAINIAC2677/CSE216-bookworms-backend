from rest_framework.permissions import BasePermission

class IsLibraryStockOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user:
            # will have to check if the user is library user or not
            return obj.library == request.user.library
        return False