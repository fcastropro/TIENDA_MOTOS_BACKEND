from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_category_icon_svg'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='brands/'),
        ),
    ]
