from rest_framework import permissions

class IsReaderAccountOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user:
            return obj.user == request.user
        return False

class IsReaderUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user:
            return request.user.groups.filter(name='reader').exists()
        return False

class HasReaderDeletePermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user:
            if obj.user == request.user:
                return True
            if obj.user.is_staff:
                return True
        return False