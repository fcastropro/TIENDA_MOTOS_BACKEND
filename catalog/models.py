from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)
    icon_svg = models.TextField(blank=True, default='')
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=80, unique=True)
    logo = models.ImageField(upload_to='brands/', null=True, blank=True)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)

    image = models.ImageField(
        upload_to='products/',
        null=True,
        blank=True,
        default='products/default.png'
    )

    def __str__(self):
        return self.name
