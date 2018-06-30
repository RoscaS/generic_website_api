import os

from django.conf import settings
from apps.gallery.models import Gallery, Image
from apps.main.models import Presentation


class Tools(object):
    @classmethod
    def build(cls):
        GenerateFake.gallery()
        GenerateFake.presentation()


class GenerateFake(object):

    @classmethod
    def presentation(cls):
        image = Image.objects.create(
            image='galleries/misc/presentation.jpg',
            gallery=Gallery.objects.get(name='misc')
        )
        Presentation.objects.create(image=image)

    @classmethod
    def gallery(cls):
        media = f'{settings.BASE_DIR}/media/galleries'
        galleries = [i for i in os.listdir(media)]
        for gallery in galleries:
            print(gallery)
            g = Gallery.objects.create(
                slug=gallery,
                name=gallery
            )
            images = [i for i in os.listdir(f'{media}/{gallery}')]
            print(f'\t{images}\n')
            for image in images:
                Image.objects.create(
                    image=f'galleries/{gallery}/{image}',
                    gallery=g)

