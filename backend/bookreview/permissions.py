from rest_framework import permissions 


class IsBookReviewerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.reviewer == request.user.reader