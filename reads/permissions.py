from rest_framework import permissions

class IsReadsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user:
            return obj.reader == request.user.reader
        return False