import os, shutil
from django.conf import settings
from django.db.models.signals import pre_delete, pre_save, post_save
from django.dispatch import receiver

from .models import Image, Gallery

@receiver(pre_delete, sender=Image)
def delete_physical_image(instance, **kwargs):
    try:
        os.remove(instance.image.path)
    except:
        pass


@receiver(post_save, sender=Image)
def set_position(instance, **kwargs):
    if kwargs['created']:
        g = Gallery.objects.get(name=instance.gallery)
        instance.position = g.images.all().count() + 1


