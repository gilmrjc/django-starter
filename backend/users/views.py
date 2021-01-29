"""
Views for the users app.
"""
from django.urls import reverse_lazy

from allauth.account.views import SignupView


class RecruiterSignupView(SignupView):
    """
    Recruitment signup view.
    """

    success_url = reverse_lazy("home")
