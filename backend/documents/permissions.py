from rest_framework.permissions import BasePermission


def is_professor(user):
    return user.role == 'professor'
class IsProfessor(BasePermission):
    """
    Allows access only to professor users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and is_professor(request.user))