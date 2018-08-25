from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Category, Article


@receiver(post_save, sender=Article)
def set_item_position(instance, **kwargs):
    if kwargs['created']:
        # print(f"\n[{instance.name}] count: {Category.objects.get(name=instance.category).items.all().count() + 1}\n")
        count = Category.objects.get(name=instance.category).articles.all().count()
        instance.position = count

# @receiver(post_save, sender=Category)
# def set_category_position(instance, **kwargs):
#     if kwargs['created']:
#         print('\n\n')
#         print('ICI')
#         print('\n\n')
#         count = Category.objects.all().count()
#         instance.position = count

