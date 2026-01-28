from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from .models import InvoiceDetail


def _get_previous(sender, instance):
    if not instance.pk:
        return None
    try:
        return sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return None


@receiver(pre_save, sender=InvoiceDetail)
def invoice_detail_update_inventory(sender, instance: InvoiceDetail, **kwargs):
    """
    Venta:
    - CREATE: resta quantity al inventory (valida stock)
    - UPDATE: ajusta por delta (valida stock)
    """
    prev = _get_previous(sender, instance)

    # CREATE
    if prev is None:
        if instance.inventory.quantity < instance.quantity:
            raise ValidationError("Stock insuficiente para esta venta.")
        instance.inventory.quantity -= instance.quantity
        instance.inventory.save(update_fields=["quantity"])
        return

    # UPDATE con cambio de inventario
    if prev.inventory_id != instance.inventory_id:
        # devolver al inventario anterior
        prev.inventory.quantity += prev.quantity
        prev.inventory.save(update_fields=["quantity"])

        # descontar en el inventario nuevo (validando stock)
        if instance.inventory.quantity < instance.quantity:
            raise ValidationError("Stock insuficiente para esta venta (inventario nuevo).")
        instance.inventory.quantity -= instance.quantity
        instance.inventory.save(update_fields=["quantity"])
    else:
        # UPDATE mismo inventario: aplicar delta de venta
        # delta > 0 => está vendiendo más (restar extra)
        # delta < 0 => está vendiendo menos (devolver stock)
        delta = instance.quantity - prev.quantity
        if delta > 0 and instance.inventory.quantity < delta:
            raise ValidationError("Stock insuficiente para aumentar la cantidad vendida.")
        if delta != 0:
            instance.inventory.quantity -= delta
            instance.inventory.save(update_fields=["quantity"])


@receiver(post_delete, sender=InvoiceDetail)
def invoice_detail_delete_inventory(sender, instance: InvoiceDetail, **kwargs):
    """
    Venta DELETE: revertir (sumar lo que se había restado)
    """
    inv = instance.inventory
    inv.quantity += instance.quantity
    inv.save(update_fields=["quantity"])
