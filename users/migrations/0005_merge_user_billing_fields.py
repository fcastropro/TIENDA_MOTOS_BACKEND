from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_billing_fields"),
        ("users", "0004_seed_roles"),
    ]

    operations = []
