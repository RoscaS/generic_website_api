# Create your models here.
import os
from pathlib import Path

from django.db import models
from django.conf import settings
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class Gallery(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(max_length=1000, null=True)
    limit = models.IntegerField(default=8)

    # images

    def path(self):
        return f'{settings.MEDIA_ROOT}/galleries/{self.name}'

    @classmethod
    def clear(cls):
        galleries = cls.objects.all()
        for gallery in galleries:
            for image in gallery.images.all():
                image.delete()
            gallery.delete()

    @classmethod
    def generate_fake(cls):
        media = f'{settings.BASE_DIR}/media/galleries'
        galleries = [i for i in os.listdir(media)]
        for gallery in galleries:
            print(gallery)
            g = Gallery.objects.create(name=gallery)
            images = [i for i in os.listdir(f'{media}/{gallery}')]
            print(f'\t{images}\n')
            for image in images:
                Image.objects.create(image=f'galleries/{gallery}/{image}',
                                     gallery=g)

    def __str__(self):
        return f'{self.name}'


def gallery_path(instance, filename):
    return f'galleries/{instance.gallery.name}/{filename}'


class Image(models.Model):
    image = models.ImageField(null=False, upload_to=gallery_path)
    description = models.TextField(max_length=1000, null=True)
    date = models.DateTimeField(auto_now_add=True)
    position = models.PositiveIntegerField(default=0)
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.image.url}'
