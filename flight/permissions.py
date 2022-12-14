from urllib import request
from rest_framework import permissions


class IsStafforReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method == permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
