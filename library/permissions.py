from rest_framework.permissions import BasePermission

class IsLibraryAccountOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user:
            return obj.user == request.user
        return False 

class IsLibraryUserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user:
            return request.user.groups.filter(name='library').exists()
        return False