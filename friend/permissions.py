from rest_framework import permissions 

class IsFriendshipOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.groups.filter(name='reader').exists():
                return (obj.friendship_from == request.user.reader or obj.friendship_to == request.user.reader)