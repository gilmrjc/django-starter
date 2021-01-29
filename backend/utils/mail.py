"""
Mail utility functions.
"""
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_templated_mail(  # pylint: disable=R0913
    subject,
    txt_template,
    html_template,
    recipient_list,
    context,
    from_email=None,
    fail_silently=False,
    auth_user=None,
    auth_password=None,
    connection=None,
):
    """
    Send an email using templates for the content.
    """
    text_body = render_to_string(txt_template, context)
    html_body = render_to_string(html_template, context)

    return send_mail(
        subject,
        text_body,
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=fail_silently,
        auth_user=auth_user,
        auth_password=auth_password,
        connection=connection,
        html_message=html_body,
    )
