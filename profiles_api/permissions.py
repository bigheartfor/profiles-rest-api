from rest_framework import permissions



class UpdateOwnProfile(permissions.BasePermission):
    """Allow yser to edit their own frofile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHOD:
            return True

        return obj.id == request.user.id
