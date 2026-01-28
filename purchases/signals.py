from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from .models import PurchaseDetail


def _get_previous(sender, instance):
    if not instance.pk:
        return None
    try:
        return sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return None


@receiver(pre_save, sender=PurchaseDetail)
def purchase_detail_update_inventory(sender, instance: PurchaseDetail, **kwargs):
    """
    Compra:
    - CREATE: suma quantity al inventory
    - UPDATE: ajusta por la diferencia (delta)
    """
    prev = _get_previous(sender, instance)
    if prev is None:
        delta = instance.quantity
        instance.inventory.quantity += delta
        instance.inventory.save(update_fields=["quantity"])
        return

    # Si cambió la bodega/inventory o la cantidad
    if prev.inventory_id != instance.inventory_id:
        # Revertir en el inventario anterior
        prev.inventory.quantity -= prev.quantity
        prev.inventory.save(update_fields=["quantity"])

        # Aplicar en el inventario nuevo
        instance.inventory.quantity += instance.quantity
        instance.inventory.save(update_fields=["quantity"])
    else:
        delta = instance.quantity - prev.quantity
        if delta != 0:
            instance.inventory.quantity += delta
            instance.inventory.save(update_fields=["quantity"])


@receiver(post_delete, sender=PurchaseDetail)
def purchase_detail_delete_inventory(sender, instance: PurchaseDetail, **kwargs):
    """
    Compra DELETE: revertir (restar lo que se había sumado)
    """
    inv = instance.inventory
    inv.quantity -= instance.quantity
    inv.save(update_fields=["quantity"])
