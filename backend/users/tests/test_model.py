"""
Tests for user model.
"""
import pytest

from ..models import User


@pytest.mark.django_db
def test_user_representation():
    """
    Test user model representation.
    """
    user = User.objects.create_user(
        username="test",
        email="test@example.com",
    )
    assert str(user) == "test@example.com"
