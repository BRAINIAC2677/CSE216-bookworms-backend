from rest_framework import permissions

class IsCommentOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.groups.filter(name='reader').exists():
                return obj.commented_by == request.user.reader
        return False