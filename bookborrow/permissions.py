from rest_framework import permissions 

class IsBookLenderPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.groups.filter(name='library').exists():
                return obj.borrowed_from == request.user.library