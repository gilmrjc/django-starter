"""
Root URL Configuration
"""
from django.conf import settings
from django.urls import path
from django.urls import include
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        include(
            [
                path("", include("pages.urls")),
                path("", include("users.urls")),
            ],
        ),
    ),
    path("anymail/", include("anymail.urls")),
    path("ht/", include("health_check.urls")),
]

if settings.DEBUG:
    from django.urls import get_callable
    from django.views import defaults

    import debug_toolbar

    urlpatterns += [
        path(
            "400/",
            defaults.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            defaults.permission_denied,
            kwargs={"exception": Exception("Permission Denied!")},
        ),
        path("403_csrf/", get_callable(settings.CSRF_FAILURE_VIEW)),
        path(
            "404/",
            defaults.page_not_found,
            kwargs={"exception": Exception("Not Found!")},
        ),
        path("500/", defaults.server_error),
    ]

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
