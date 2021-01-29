"""
Tests for pages views.
"""
from django.urls import reverse
from django.contrib.auth import get_user_model

import pytest

User = get_user_model()


@pytest.mark.django_db
def test_home_view_success(client):
    """
    Test home page success render.
    """
    user = User.objects.create_user(username="test", email="test@example.com")
    client.force_login(user)

    url = reverse("home")
    response = client.get(url)

    assert response.status_code == 200
