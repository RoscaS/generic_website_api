import os, shutil
from pathlib import Path

from django.conf import settings
from django.db import models


class Gallery(models.Model):
    slug = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(max_length=100, null=True)
    limit = models.IntegerField(default=8)

    def set_placeholder(self):
        static = settings.STATIC_ROOT
        media = settings.MEDIA_ROOT
        dest = Path(os.path.join(media, 'galleries', 'placeholders'))
        if not Path.exists(dest):
            os.mkdir(dest)
        name = f"placeholder_{self.name}"
        shutil.copy(f"{static}/placeholder.jpg", os.path.join(dest, name))
        return Image.objects.create(image=f"galleries/placeholders/{name}",
                                    gallery=self,
                                    name=name)

    def path(self):
        return f'{settings.MEDIA_ROOT}/galleries/{self.name}'

    def __str__(self):
        return f'{self.name}'


def gallery_path(instance, filename):
    if instance.gallery.name == '_temp':
        return f'galleries/{instance.gallery.name}/{filename}'
    return f'galleries/{filename}'


class Image(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=False, upload_to=gallery_path)
    description = models.TextField(max_length=1000, null=True)
    date = models.DateTimeField(auto_now_add=True)
    gallery = models.ForeignKey(Gallery, related_name='images',
                                on_delete=models.CASCADE)
    position = models.PositiveIntegerField(default=0)

    class meta:
        ordering = ['image']

    def __str__(self):
        return f'{self.name}'
