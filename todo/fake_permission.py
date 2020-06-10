from rest_framework import permissions


class FakePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True
