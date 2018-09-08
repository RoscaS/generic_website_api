from django.db import models
from django.core.validators import MinValueValidator
from apps.gallery.models import Image

class Category(models.Model):
    slug = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    position = models.PositiveIntegerField(default=0)

    def __str__(self):

        return f'{self.name}'

def gallery_path(instance, filename):
    if instance.gallery.name == '_temp':
        return f'galleries/{instance.gallery.name}/{filename}'
    return f'galleries/{filename}'


class Article(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True)
    price = models.FloatField(default=.0, null=False, validators=[MinValueValidator(.0)])
    description = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(Category, related_name="articles", on_delete=models.CASCADE)
    image = models.OneToOneField(Image, related_name='article', blank=False, null=False, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


