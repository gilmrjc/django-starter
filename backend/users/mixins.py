"""
Mixins for user app.
"""


from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import UserPassesTestMixin


class UserIsStaffMixin:  # pylint: disable=R0903
    """
    Mixin to check if user is staff.
    """

    def is_staff(self):
        """
        Check if user is staff.
        """
        return self.request.user.is_staff


class StaffAccessOnly(
    UserIsStaffMixin,
    UserPassesTestMixin,
):
    """
    Mixing to allow access only to staff users.
    """

    def test_func(self):
        return self.is_staff()

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse("home"))
