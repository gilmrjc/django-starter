"""
Django settings for core project.
"""

import os

from configurations import Configuration
from configurations import values

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Base(Configuration):
    """
    Base settings.
    """

    # pylint: disable=W0232
    DEBUG = False
    PRODUCTION = False

    SECRET_KEY = "very-insecure-secret"

    DJANGO_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.sites",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ]
    THIRD_PARTY_APPS = [
        "allauth",
        "allauth.account",
        "anymail",
        "django_extensions",
        "django_q",
        "health_check",
        "health_check.db",
        "health_check.cache",
        "health_check.storage",
        "health_check.contrib.migrations",
        "storages",
        "widget_tweaks",
    ]
    LOCAL_APPS = [
        "pages",
        "seed",
        "users",
        "utils",
    ]

    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

    # Application definition

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ROOT_URLCONF = "core.urls"

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [os.path.join(BASE_DIR, "templates")],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                    "django_settings_export.settings_export",
                ],
            },
        },
    ]

    WSGI_APPLICATION = "core.wsgi.application"

    SITE_ID = 1

    DATABASES = values.DatabaseURLValue()
    CACHES = values.CacheURLValue()

    Q_CLUSTER = {
        "timeout": 180,
        "retry": 190,
        "django_redis": "default",
        "error_reporter": {},
    }

    AUTH_USER_MODEL = "users.User"
    LOGIN_URL = "account_login"

    ACCOUNT_AUTHENTICATION_METHOD = "email"
    LOGIN_REDIRECT_URL = "home"

    ACCOUNT_USERNAME_REQUIRED = False
    ACCOUNT_UNIQUE_EMAIL = True
    ACCOUNT_PRESERVE_USERNAME_CASING = False
    ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False

    ACCOUNT_LOGOUT_ON_GET = True
    ACCOUNT_LOGOUT_REDIRECT_URL = "account_login"

    # Password validation
    # https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501 pylint: disable=C0301
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa: E501 pylint: disable=C0301
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa: E501 pylint: disable=C0301
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa: E501 pylint: disable=C0301
        },
    ]

    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend",
    )

    # Internationalization
    # https://docs.djangoproject.com/en/3.0/topics/i18n/

    LANGUAGE_CODE = "es-mx"

    TIME_ZONE = "UTC"

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.0/howto/static-files/

    STATICFILES_DIRS = [os.path.join(BASE_DIR, "assets")]

    STATIC_LOCATION = "static"
    STATIC_URL = "/static/"
    STATIC_ROOT = os.path.join(BASE_DIR, "static")

    PUBLIC_MEDIA_LOCATION = "media"
    PRIVATE_MEDIA_LOCATION = "private"
    MEDIA_URL = values.URLValue("http://localhost:8080/media/")
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
    # pylint: disable=E1101
    PRIVATE_FILE_STORAGE = Configuration.DEFAULT_FILE_STORAGE

    # Instrumentation

    SETTINGS_EXPORT = [
        "DEBUG",
        "PRODUCTION",
    ]


class Dev(Base):
    """
    Development settings.
    """

    # pylint: disable=W0232
    DEBUG = True

    SECRET_KEY = "very-insecure-token"
    EMAIL_BACKEND = "mail_panel.backend.MailToolbarBackend"

    INSTALLED_APPS = Base.INSTALLED_APPS + [
        "debug_toolbar",
        "mail_panel",
    ]

    MIDDLEWARE = [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ] + Base.MIDDLEWARE

    DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda request: True}

    DEBUG_TOOLBAR_PANELS = [
        "debug_toolbar.panels.history.HistoryPanel",
        "debug_toolbar.panels.versions.VersionsPanel",
        "debug_toolbar.panels.timer.TimerPanel",
        "debug_toolbar.panels.settings.SettingsPanel",
        "mail_panel.panels.MailToolbarPanel",
        "debug_toolbar.panels.headers.HeadersPanel",
        "debug_toolbar.panels.request.RequestPanel",
        "debug_toolbar.panels.sql.SQLPanel",
        "debug_toolbar.panels.staticfiles.StaticFilesPanel",
        "debug_toolbar.panels.templates.TemplatesPanel",
        "debug_toolbar.panels.cache.CachePanel",
        "debug_toolbar.panels.signals.SignalsPanel",
        "debug_toolbar.panels.logging.LoggingPanel",
        "debug_toolbar.panels.redirects.RedirectsPanel",
        "debug_toolbar.panels.profiling.ProfilingPanel",
    ]

    ALLOWED_HOSTS = ["*"]


class Testing(Base):
    """
    Testing settings.
    """

    # pylint: disable=W0232
    DATABASES = values.DatabaseURLValue(
        "sqlite://:memory:",
        environ_name="TESTING_DATABASE_URL",
    )
    EMAIL = values.EmailURLValue("memory://", environ_name="TESTING_EMAIL_URL")
    CACHES = values.CacheURLValue(
        "locmem://",
        environ_name="TESTING_CACHE_URL",
    )


class IntegrationTesting(Base):
    """
    Integration testing settings.
    """

    # pylint: disable=W0232
    ALLOWED_HOSTS = ["*"]

    CACHES = values.CacheURLValue("locmem://")
    Q_CLUSTER = {
        "workers": 1,
        "timeout": 90,
        "retry": 100,
        "orm": "default",
        "sync": True,
        "scheduler": False,
    }

    EMAIL = values.EmailURLValue()
    DEFAULT_FROM_EMAIL = "mail@example.com"

    STATIC_URL = values.URLValue("http://localhost:8080/static/")
    MEDIA_URL = values.URLValue("http://localhost:8080/media/")


class Production(Base):
    """
    Production settings.
    """

    # pylint: disable=W0232
    PRODUCTION = True
    ALLOWED_HOSTS = values.ListValue()
    SECRET_KEY = values.SecretValue()

    SITE_ID = values.SecretValue()

    DEFAULT_FROM_EMAIL = values.SecretValue()
    SERVER_EMAIL = values.SecretValue()

    # Set email configuration
    # EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"

    # storage settings
    AWS_ACCESS_KEY_ID = values.SecretValue(environ_prefix="")
    AWS_SECRET_ACCESS_KEY = values.SecretValue(environ_prefix="")
    AWS_STORAGE_BUCKET_NAME = values.SecretValue(environ_prefix="")
    AWS_S3_REGION_NAME = "nyc3"

    AWS_S3_ENDPOINT_URL = (
        f"https://{AWS_S3_REGION_NAME}.digitaloceanspaces.com"  # noqa: E501
    )

    AWS_DEFAULT_ACL = None

    # s3 static settings
    STATIC_LOCATION = "static"
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/"
    STATICFILES_STORAGE = "utils.storage.StaticStorage"

    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = "media"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/"
    DEFAULT_FILE_STORAGE = "utils.storage.PublicMediaStorage"

    # s3 private media settings
    PRIVATE_MEDIA_LOCATION = "private"
    PRIVATE_FILE_STORAGE = "utils.storage.PrivateMediaStorage"
