from django.db import migrations
from django.contrib.auth import get_user_model


def create_superuser(apps, schema_editor):
    User = get_user_model()
    User.objects.create_superuser(email='u@u.com', password='u', name='u')


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
