"""
Tests for utils.
"""
import random
from unittest import mock

from django.db import models

from .models import SlugMixin
from .models import instance_unique_slug
from .models import random_string_generator


def test_random_string_generator():
    """
    Test random string generator default behaviour.
    """
    random.seed(0)

    result = next(random_string_generator())

    assert result == "mynbiq"


def test_random_string_generator_length():
    """
    Test custom length random string.
    """
    random.seed(0)

    result = next(random_string_generator(10))

    assert result == "mynbiqpmzj"


def test_random_string_generator_base():
    """
    Test custom dictionary for random string generator.
    """
    result = next(random_string_generator(3, "a"))

    assert result == "aaa"


@mock.patch("utils.models.models.query.QuerySet.exists")
def test_unique_slug(queryset_mock):
    """
    Test the unique slug function using a test instance.
    """
    random.seed(0)
    queryset_mock.return_value = False

    class TestModel(SlugMixin):
        """
        Test model used to check slug generation.
        """

        name = models.CharField(max_length=150, verbose_name="nombre")
        slug = models.CharField(max_length=150, blank=True, editable=False)

    test = TestModel(name="Test")
    slug = instance_unique_slug(test)

    assert slug == "test-mynbiq"


@mock.patch("utils.models.models.query.QuerySet.exists")
def test_unique_slug_collision(queryset_mock):
    """
    Test the unique slug function when there are collisions.
    """
    random.seed(0)
    queryset_mock.side_effect = [True, False]

    class TestModel(SlugMixin):
        """
        Test model used to check slug generation.
        """

        name = models.CharField(max_length=150, verbose_name="nombre")
        slug = models.CharField(max_length=150, blank=True, editable=False)

    test = TestModel(name="Test")
    slug = instance_unique_slug(test)

    assert slug == "test-pmzjpl"


@mock.patch("utils.models.models.Model.save")
@mock.patch("utils.models.models.query.QuerySet.exists")
def test_slug_mixin_save(queryset_mock, model_mock):
    """
    Test unique slug behaviour on models.
    """
    random.seed(0)
    queryset_mock.return_value = False

    class TestModel(SlugMixin):
        """
        Test model used to check slug generation.
        """

        name = models.CharField(max_length=150, verbose_name="nombre")
        slug = models.CharField(max_length=150, blank=True, editable=False)

    test = TestModel.objects.create(name="Test")

    assert test.slug == "test-mynbiq"
    model_mock.assert_called_once()


@mock.patch("utils.models.models.Model.save")
@mock.patch("utils.models.models.query.QuerySet.exists")
def test_slug_mixin_update_slug(queryset_mock, model_mock):
    """
    Test update slug behaviour on models.
    """
    random.seed(0)
    queryset_mock.return_value = False

    class TestModel(SlugMixin):
        """
        Test model used to check slug generation.
        """

        name = models.CharField(max_length=150, verbose_name="nombre")
        slug = models.CharField(max_length=150, blank=True, editable=False)

    test = TestModel(name="Test")
    test.update_slug("new slug")

    assert test.slug == "new-slug"
    model_mock.assert_called_once()


@mock.patch("utils.models.models.Model.save")
@mock.patch("utils.models.models.query.QuerySet.exists")
def test_slug_mixin_update_slug_collision(queryset_mock, model_mock):
    """
    Test update slug behaviour on models when a collision occurs.
    """
    random.seed(0)
    queryset_mock.side_effect = [True, False]

    class TestModel(SlugMixin):
        """
        Test model used to check slug generation.
        """

        name = models.CharField(max_length=150, verbose_name="nombre")
        slug = models.CharField(max_length=150, blank=True, editable=False)

    test = TestModel(name="Test")
    test.update_slug("new slug")

    assert test.slug == "test-mynbiq"
    model_mock.assert_called_once_with()


@mock.patch("utils.models.models.Model.save")
@mock.patch("utils.models.models.query.QuerySet.exists")
def test_slug_mixin_custom_string_generator(queryset_mock, model_mock):
    """
    Test a custom unique slug generator using a test instance.
    """
    random.seed(0)
    queryset_mock.return_value = False

    class TestModel(SlugMixin):
        """
        Test model used to check slug generation.
        """

        RANDOM_STRING_GENERATOR = random_string_generator(2, "ab")

        name = models.CharField(max_length=150, verbose_name="nombre")
        slug = models.CharField(max_length=150, blank=True, editable=False)

    test = TestModel.objects.create(name="Test")

    assert test.slug == "test-bb"
    model_mock.assert_called_once()
