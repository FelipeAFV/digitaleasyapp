from rest_framework.permissions import BasePermission

class RolePermission(BasePermission):
    def has_permission(self, request, view, role_name):

        return request.user.role_name == role_name


