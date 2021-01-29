"""
Pages app. Here are the generic pages needed for the project.
"""
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """
    Home page view.
    """

    template_name = "pages/home.html"
