from django.db import migrations


def seed_roles(apps, schema_editor):
    Role = apps.get_model('users', 'Role')
    Role.objects.get_or_create(name='cliente')
    Role.objects.get_or_create(name='administrador')


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_auth_fields'),
    ]

    operations = [
        migrations.RunPython(seed_roles),
    ]
