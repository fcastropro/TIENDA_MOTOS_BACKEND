from django.db import models
from catalog.models import Product
from inventory.models import Inventory

class Supplier(models.Model):
    name = models.CharField(max_length=120)
    ruc = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"Compra #{self.id}"


class PurchaseDetail(models.Model):
    purchase = models.ForeignKey(
        Purchase,
        on_delete=models.CASCADE,
        related_name='details'
    )
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    inventory = models.ForeignKey(Inventory, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
