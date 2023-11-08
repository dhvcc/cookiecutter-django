from django.conf import settings

{%- if cookiecutter.use_allauth == 'y' %}
def allauth_settings(request):
    """Expose some settings from django-allauth in templates."""
    return {
        "ACCOUNT_ALLOW_REGISTRATION": settings.ACCOUNT_ALLOW_REGISTRATION,
    }
{%- endif %}
