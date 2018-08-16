from django.db import models
from django.core.validators import MinValueValidator
from apps.gallery.models import Image

class Category(models.Model):
    slug = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=1000, null=True)
    position = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.name}'


class Item(models.Model):
    # slug = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    price = models.FloatField(default=.0, validators=[MinValueValidator(.0)])
    description = models.CharField(max_length=400)
    category = models.ForeignKey(Category, related_name="articles", on_delete=models.CASCADE)
    image = models.OneToOneField(Image, related_name='article', blank=True, null=True, on_delete=models.SET_NULL)
    position = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.name}'
