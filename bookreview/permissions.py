from rest_framework import permissions 

class IsBookReviewerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.groups.filter(name='reader').exists():
                return obj.reviewer == request.user.reader