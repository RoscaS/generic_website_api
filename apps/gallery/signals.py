import os
from django.db.models.signals import pre_delete, pre_save, post_save
from django.dispatch import receiver

from .models import Image, Gallery

@receiver(pre_delete, sender=Image)
def delete_physical_image(instance, **kwargs):
    try:
        os.remove(instance.image.path)
    except:
        pass

@receiver(pre_save, sender=Image)
def set_position(instance, **kwargs):
    g = Gallery.objects.get(name=instance.gallery)
    instance.position = g.images.all().count() + 1

