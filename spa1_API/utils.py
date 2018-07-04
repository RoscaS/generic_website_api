import os

import forgery_py

from django.conf import settings
from apps.gallery.models import Gallery, Image
from apps.main.models import PresentationSection, HeroSection, GallerySection, \
    ContactSection, MainOptions, ReviewSection


def sentences(n):
    return forgery_py.lorem_ipsum.sentences(n).capitalize()


class Tools(object):
    @classmethod
    def build(cls):
        MainOptions.objects.create()

        GenerateFake.gallery()
        GenerateFake.presentation()
        HeroSection.objects.create()
        GallerySection.objects.create()
        ContactSection.objects.create()
        ReviewSection.objects.create()


class GenerateFake(object):

    @classmethod
    def presentation(cls):
        image = Image.objects.create(
            image='galleries/misc/presentation.jpg',
            gallery=Gallery.objects.get(name='misc')
        )
        PresentationSection.objects.create(image=image)

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
                    description=sentences(1),
                    gallery=g
                )

        descriptions = ['Articles', 'Galerie', 'Contact']
        parallax = Image.objects.filter(gallery__name='parallax')
        for c, i in enumerate(parallax):
            i.description = descriptions[c]
            i.save()

        # Image.objects.get(id=1).description = 'Articles'.upper()
        # Image.objects.get(id=2).description = 'Gallerie'.upper()
        # Image.objects.get(id=3).description = 'Contact'.upper()
