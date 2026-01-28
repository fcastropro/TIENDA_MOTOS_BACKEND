from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon_svg',
            field=models.TextField(blank=True, default=''),
        ),
    ]
