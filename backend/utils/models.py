"""
Utility models.
"""
from django.db import models
from django.utils.text import slugify

from django_extensions.db.fields import CreationDateTimeField
from django_extensions.db.fields import ModificationDateTimeField

from .utils import random_string_generator

DEFAULT_GENERATOR = random_string_generator()


def instance_unique_slug(
    instance,
    name_field="name",
    slug_field="slug",
    value=None,
    rsg=DEFAULT_GENERATOR,
):
    """
    Take an instance and generate a unique slug for it.
    """
    if value is not None:
        new_slug = slugify(value)
    else:
        # We are using .lower() method for case insensitive
        field_value = getattr(instance, name_field)
        slug = slugify(field_value.lower())

        rand_str = next(rsg)
        new_slug = f"{slug}-{rand_str}"

    klass = instance.__class__
    qs_exists = klass.objects.filter(**{slug_field: new_slug}).exists()

    if qs_exists:
        return instance_unique_slug(instance, name_field, slug_field, None)

    return new_slug


class SlugMixin(models.Model):
    """
    Mixing for models to autogenerate a slug on instance save.
    """

    NAME_FIELD = "name"
    SLUG_FIELD = "slug"
    RANDOM_STRING_GENERATOR = DEFAULT_GENERATOR

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):  # pylint: disable=signature-differs
        if not getattr(self, self.SLUG_FIELD):
            self.slug = instance_unique_slug(
                self,
                self.NAME_FIELD,
                self.SLUG_FIELD,
                None,
                self.RANDOM_STRING_GENERATOR,
            )

        super().save(*args, **kwargs)

    def update_slug(self, new_slug):
        """
        Update slug to a custom one. Respects the unique constraint.
        """
        self.slug = instance_unique_slug(
            self,
            self.NAME_FIELD,
            self.SLUG_FIELD,
            new_slug,
            self.RANDOM_STRING_GENERATOR,
        )

        self.save()


class TimeStampedMixin(models.Model):
    """
    Mixin for models to add timestamp fields.
    """

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        abstract = True
