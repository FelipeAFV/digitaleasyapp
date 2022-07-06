from rest_framework.permissions import BasePermission
from .models import User

class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.role:
            return False

        return request.user.role == User.ADMIN

class ClientPermission(BasePermission):
    def has_permission(self, request, view):

        if request.user.is_superuser:
            return True

        if not request.user.role:
            return False

        return request.user.role == User.CLIENT


