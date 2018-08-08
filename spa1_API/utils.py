import os
import shutil

import forgery_py

from django.conf import settings
from django.contrib.auth.models import User
from apps.gallery import models as gallery
from apps.main import models as main


simple_models = [
    main.HeroSection,
    main.GallerySection,
    main.ContactSection,
    main.ReviewSection,
    main.MainOptions,
]


def sentences(n):
    return forgery_py.lorem_ipsum.sentences(n).capitalize()

class Tools(object):

    @classmethod
    def reset_media(cls):
        media = f'{settings.BASE_DIR}/media/galleries'
        shutil.rmtree(media)
        os.mkdir(media)
        os.mkdir(f"{media}/_temp")

        # for el in os.listdir(media):
        #     try:
        #         os.remove(f"{media}/{el}")
        #     except:
        #         shutil.rmtree(f"{media}/{el}")


        #
        # galleries = [i for i in os.listdir(_media)]
        #
        # for gallery in galleries:
        #     for image in os.listdir(f"{_media}/{gallery}"):

        # for gallery in galleries:
        #     for image in os.listdir(f"{media}/{gallery}"):
        #         os.remove(f"{media}/{gallery}/{image}")
        #     print(f"Folder '{gallery}': Cleared.")
        #
        #     _media = media.replace('media', '_media')
        #     for image in os.listdir(f"{_media}/{gallery}"):
        #         shutil.copy(f"{_media}/{gallery}/{image}",
        #                     f"{media}/{gallery}/{image}")
        #     print(f"Folder '{gallery}': Reinitialized.")

    @classmethod
    def admin(cls):
        User.objects.create_superuser(
            username='admin',
            email='jrosk.ad@gmail.com',
            password='solsolsol'
        )
        print("User 'admin': Created.")

    @classmethod
    def build(cls):
        cls.admin()
        cls.reset_media()
        GenerateFake.gallery()
        GenerateFake.presentation()
        GenerateFake.promo()

        for i in simple_models:
            i.objects.create()
            print(f"Model {i.__name__}: Created.")


class GenerateFake(object):
    @classmethod
    def promo(cls):
        image = gallery.Image.objects.create(
            image='galleries/misc/action.jpg',
            gallery=gallery.Gallery.objects.get(name='misc')
        )
        main.PromoSection.objects.create(image=image)
        print("Fake Promo model: Created.")

    @classmethod
    def presentation(cls):
        image = gallery.Image.objects.create(
            image='galleries/misc/presentation.jpg',
            gallery=gallery.Gallery.objects.get(name='misc')
        )
        main.PresentationSection.objects.create(image=image)
        print("Fake Presentation model: Created.")

    # @classmethod
    # def promo(cls):
    #     main.PromoSection.objects.create(image=gallery.Image.objects.get(name='0023.jpg'))
    #     print("Fake Promo model: Created.")
    #
    # @classmethod
    # def presentation(cls):
    #     main.PresentationSection.objects.create(image=gallery.Image.objects.get(name='0024.jpg'))
    #     print("Fake Presentation model: Created.")

    @classmethod
    def gallery(cls):
        media = f'{settings.BASE_DIR}/media/galleries'
        _media = f'{settings.BASE_DIR}/_media/galleries'
        galleries = [i for i in os.listdir(_media)]
        print(galleries)
        galleries.pop(galleries.index('misc'))
        print(galleries)

        count = 1
        print('Galleries:')
        for i in galleries:
            print(f"{4*' '}{i}", end=": ")
            g = gallery.Gallery.objects.create(
                slug=i,
                name=i
            )
            images = sorted([i for i in os.listdir(f'{_media}/{i}')])
            for pos, j in enumerate(images):
                name = "{:04d}.{}".format(count, j.split('.')[-1])
                shutil.copy(f'{_media}/{i}/{j}', f'{media}/{name}')
                print(name)
                gallery.Image.objects.create(
                    name = name,
                    image=f'galleries/{name}',
                    description=sentences(1),
                    gallery=g,
                )
                count += 1

        gallery.Gallery.objects.create(slug='misc', name='misc')
        shutil.copytree(f'{_media}/misc', f'{media}/misc')


        descriptions = ['Articles', 'Galerie', 'Contact']
        parallax = gallery.Image.objects.filter(gallery__name='parallax')
        for c, i in enumerate(parallax):
            i.description = descriptions[c]
            i.save()

