from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Category, Article


@receiver(post_save, sender=Article)
def set_item_position(instance, **kwargs):
    if kwargs['created']:
        count = Category.objects.get(name=instance.category).articles.all().count()
        instance.position = count

