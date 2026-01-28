from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
