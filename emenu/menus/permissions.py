from rest_framework import permissions


class MenuPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ["GET"]:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "PUT", "PATCH", "DELETE"] and request.user.is_authenticated:
            return True
        return False
