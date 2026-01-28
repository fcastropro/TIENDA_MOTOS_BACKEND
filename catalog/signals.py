import os
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .models import Product, Brand


def _delete_file(path: str):
    if path and os.path.isfile(path):
        os.remove(path)


@receiver(pre_save, sender=Product)
def delete_old_image_on_change(sender, instance: Product, **kwargs):
    """
    Si se actualiza un Product y cambia la imagen, elimina la imagen anterior del disco.
    """
    if not instance.pk:
        return  # es creación, no hay imagen anterior

    try:
        old = Product.objects.get(pk=instance.pk)
    except Product.DoesNotExist:
        return

    old_image = old.image
    new_image = instance.image

    # Si no cambió la imagen, no hacemos nada
    if not old_image:
        return
    if old_image == new_image:
        return

    # No borrar si la imagen vieja es la default
    if old_image.name == 'products/default.png':
        return

    # Borrar archivo viejo
    _delete_file(old_image.path)


@receiver(post_delete, sender=Product)
def delete_image_on_delete(sender, instance: Product, **kwargs):
    """
    Si borras el producto, borra también su imagen del disco (excepto la default).
    """
    img = instance.image
    if not img:
        return
    if img.name == 'products/default.png':
        return
    _delete_file(img.path)


@receiver(pre_save, sender=Brand)
def delete_old_logo_on_change(sender, instance: Brand, **kwargs):
    """
    Si se actualiza una Brand y cambia el logo, elimina el anterior del disco.
    """
    if not instance.pk:
        return  # es creación, no hay logo anterior

    try:
        old = Brand.objects.get(pk=instance.pk)
    except Brand.DoesNotExist:
        return

    old_logo = old.logo
    new_logo = instance.logo

    if not old_logo:
        return
    if old_logo == new_logo:
        return

    _delete_file(old_logo.path)


@receiver(post_delete, sender=Brand)
def delete_logo_on_delete(sender, instance: Brand, **kwargs):
    """
    Si borras la marca, borra también su logo del disco.
    """
    logo = instance.logo
    if not logo:
        return
    _delete_file(logo.path)
