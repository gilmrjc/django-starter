"""
Storage backends for core project.
"""
import os
import re
import posixpath
from urllib.parse import unquote
from urllib.parse import urldefrag

from django.db import models
from django.conf import settings
from django.utils.module_loading import import_string
from django.contrib.staticfiles.storage import HashedFilesMixin
from django.contrib.staticfiles.storage import ManifestFilesMixin

from storages.backends.s3boto3 import S3Boto3Storage


class ESModulesHashedFilesMixin(HashedFilesMixin):
    """
    Set the correct url on es module imports.
    """

    def __init__(self, *args, **kwargs):
        self.patterns = (
            *self.patterns,
            (
                "*.js",
                (
                    (
                        r"""(import\s*(.*?)\s*from\s*["'](.*?)["'])""",
                        ("""import %s from '%s'"""),
                    ),
                ),
            ),
        )
        super().__init__(*args, **kwargs)

    def url_converter(self, name, hashed_files, template=None):
        """
        Return the custom URL converter for the given file name.
        """

        def js_converter(matchobj):
            matched, imports, url = matchobj.groups()

            # Ignore absolute/protocol-relative and data-uri URLs.
            if re.match(r"^[a-z]+:", url):
                return matched

            # Ignore absolute URLs that don't point to a static file (dynamic
            # CSS / JS?). Note that STATIC_URL cannot be empty.
            if url.startswith("/") and not url.startswith(settings.STATIC_URL):
                return matched

            # Strip off the fragment so a path-like fragment won't interfere.
            url_path, fragment = urldefrag(url)

            if url_path.startswith("/"):
                assert url_path.startswith(settings.STATIC_URL)
                static_url_len = len(settings.STATIC_URL)
                target_name = url_path[static_url_len:]
            else:
                # We're using the posixpath module to mix paths and URLs
                # conveniently.
                source_name = (
                    name if os.sep == "/" else name.replace(os.sep, "/")
                )
                target_name = posixpath.join(
                    posixpath.dirname(source_name),
                    url_path,
                )

            # Determine the hashed name of the target file with the storage
            # backend.
            hashed_url = self._url(
                self._stored_name,
                unquote(target_name),
                force=True,
                hashed_files=hashed_files,
            )

            transformed_url = "/".join(
                url_path.split("/")[:-1] + hashed_url.split("/")[-1:],
            )

            # Restore the fragment that was stripped off earlier.
            if fragment:
                transformed_url += ("?#" if "?#" in url else "#") + fragment

            # Return the hashed version to the file
            return template % (imports, unquote(transformed_url))

        _, ext = os.path.splitext(name)
        if ext == ".js":
            return js_converter

        return super().url_converter(name, hashed_files, template)


class StaticStorage(
    ESModulesHashedFilesMixin,
    ManifestFilesMixin,
    S3Boto3Storage,
):
    """
    Storage configuration for static files.
    """

    # pylint: disable=W0223
    location = settings.STATIC_LOCATION
    default_acl = "public-read"
    gzip = True
    object_parameters = {"CacheControl": "15758000"}


class PublicMediaStorage(S3Boto3Storage):
    """
    Storage configuration for public media files.
    """

    # pylint: disable=W0223
    location = settings.PUBLIC_MEDIA_LOCATION
    default_acl = "public-read"
    file_overwrite = False


class PrivateMediaStorage(S3Boto3Storage):
    """
    Storage configuration for private media files.
    """

    # pylint: disable=W0223
    location = settings.PRIVATE_MEDIA_LOCATION
    default_acl = "private"
    file_overwrite = False
    custom_domain = False


def get_private_storage():
    """
    Get private storage class. When running with DEBUG use the default storage
    class.
    """
    if settings.DEBUG:
        return import_string(settings.DEFAULT_FILE_STORAGE)()

    return import_string(settings.PRIVATE_FILE_STORAGE)()


class PrivateFileField(models.FileField):
    """
    File field configured to use the private storage class.
    """

    def __init__(self, *args, **kwargs):
        """
        Set custom storage on class init.
        """
        kwargs["storage"] = get_private_storage()
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        """
        Remove storage name from deconstruct to make the implementation
        flexible.
        """
        name, path, args, kwargs = super().deconstruct()
        del kwargs["storage"]
        return name, path, args, kwargs

    def generate_filename(self, instance, filename):  # pragma: no cover
        """
        Add the word "private" to the root when DEBUG is True. otherwise keep
        the original filename generation logic.
        """
        filename = super().generate_filename(instance, filename)

        if settings.DEBUG:
            filename = f"private/{filename}"

        return filename
