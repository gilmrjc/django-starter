"""
URLs for the users app.
"""
from django.urls import path
from django.urls import re_path

from allauth.account import views

from .views import RecruiterSignupView

urlpatterns = [
    path(
        "crear-cuenta/",
        RecruiterSignupView.as_view(),
        name="account_signup",
    ),
    path("iniciar-sesion/", views.login, name="account_login"),
    path("cerrar-sesion/", views.logout, name="account_logout"),
    path(
        "password/cambiar/",
        views.password_change,
        name="account_change_password",
    ),
    path(
        "password/establecer/",
        views.password_set,
        name="account_set_password",
    ),
    path("inactivo/", views.account_inactive, name="account_inactive"),
    # E-mail
    path("email/", views.email, name="account_email"),
    path(
        "confirmar-email/",
        views.email_verification_sent,
        name="account_email_verification_sent",
    ),
    re_path(
        r"^confirmar-email/(?P<key>[-:\w]+)/$",
        views.confirm_email,
        name="account_confirm_email",
    ),
    # password reset
    path(
        "password/reestablecer/",
        views.password_reset,
        name="account_reset_password",
    ),
    path(
        "password/reestablecer/terminado/",
        views.password_reset_done,
        name="account_reset_password_done",
    ),
    re_path(
        r"^password/reestablecer/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        views.password_reset_from_key,
        name="account_reset_password_from_key",
    ),
    path(
        "password/reestablecer/key/terminado/",
        views.password_reset_from_key_done,
        name="account_reset_password_from_key_done",
    ),
]
