import os
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from . import models

@receiver(pre_delete, sender=models.Image)
def delete_physical_image(instance, **kwargs):
    try:
        os.remove(instance.image.path)
    except:
        pass
