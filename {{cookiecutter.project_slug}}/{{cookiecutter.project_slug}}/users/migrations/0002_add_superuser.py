from django.db import migrations
from django.contrib.auth import get_user_model


def create_superuser(apps, schema_editor):
    User = get_user_model()
    {%- if cookiecutter.username_type == "username" %}
    User.objects.create_superuser(password='u', email='', username='u')
    {%- elif cookiecutter.username_type == "email" %}
    User.objects.create_superuser(email='u@u.com', password='u', name='u')
    {%- endif %}


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
