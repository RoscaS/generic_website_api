import os, shutil, forgery_py
from random import randint, seed

from django.conf import settings
from django.contrib.auth.models import User
from apps.gallery import models as gallery
from apps.main import models as main
from apps.articles import models as articles
from apps.time import models as time

simple_models = [
    main.HeroSection,
    main.EventsSection,
    main.ArticlesSection,
    main.ContactSection,
    main.ReviewSection,
    main.SiteOptions,
    main.SiteInformations,
    main.SiteContact,
]

media = f'{settings.BASE_DIR}/media/galleries'
_media = f'{settings.BASE_DIR}/_media/galleries'


def sentences(n):
    return forgery_py.lorem_ipsum.sentences(n).capitalize()


class Tools(object):
    @classmethod
    def reset_media(cls):
        shutil.rmtree(media)
        os.mkdir(media)
        os.mkdir(f"{media}/_temp")

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
        GenerateFake.articles()
        GenerateFake.presentation()
        GenerateFake.promo()
        GenerateFake.time()

        for i in simple_models:
            i.objects.create()
            print(f"Model {i.__name__}: Created.")


class GenerateFake(object):

    @classmethod
    def time(cls):
        WEEKDAYS = [
            "lundi",
            "mardi",
            "mercredi",
            "jeudi",
            "vendredi",
            "samedi",
            "dimanche",
        ]
        for day in WEEKDAYS:
            time.Day.objects.create(name=day, slug=day)

    @classmethod
    def articles(cls):
        names = []
        images = gallery.Gallery.objects.get(name='Articles').images.all()
        counter = images.count()

        word = lambda: forgery_py.lorem_ipsum.word().capitalize()
        for category in [word() for i in range(4)]:
            seed()
            description = forgery_py.lorem_ipsum.words(randint(3, 5)),
            cat = articles.Category.objects.create(
                slug=category,
                name=category,
                description=description[0].capitalize() + '.'
            )
            cat.save()
            for item in range(6):
                counter -= 1
                description = forgery_py.lorem_ipsum.words(randint(3, 5)),
                name = 'Shufflebeat'
                while name in names:
                    name = forgery_py.name.company_name()
                names.append(name)

                article = articles.Article.objects.create(
                    name=name,
                    price=float(f"{randint(5, 20)}.{randint(0, 99)}"),
                    description=description[0].capitalize() + '.',
                    category=cat,
                    image=images[counter]
                )
                article.save()

    @classmethod
    def promo(cls):
        promo_gallery = gallery.Gallery.objects.get(name='Promo')
        main.PromoSection.objects.create()
        promo_gallery.limit = 1
        promo_gallery.save()
        print("Fake Promo model: Created.")

    @classmethod
    def presentation(cls):
        presentation_gallery = gallery.Gallery.objects.get(name='Presentation')
        main.PresentationSection.objects.create()
        presentation_gallery.limit = 1
        presentation_gallery.save()
        print("Fake Presentation model: Created.")

    @classmethod
    def gallery(cls):
        galleries = [i for i in os.listdir(_media)]
        count = 1
        print('Galleries:')
        for i in galleries:
            print(f"{4*' '}{i}", end=": ")
            g = gallery.Gallery.objects.create(
                slug=i.capitalize(),
                name=i.capitalize()
            )
            images = sorted([i for i in os.listdir(f'{_media}/{i}')])
            for j in images:
                name = "{:04d}.{}".format(count, j.split('.')[-1])
                shutil.copy(f'{_media}/{i}/{j}', f'{media}/{name}')
                print(name)
                gallery.Image.objects.create(
                    name=name,
                    image=f'galleries/{name}',
                    description=sentences(1),
                    gallery=g,
                )
                count += 1

        descriptions = ['Articles', 'Galerie', 'Contact']
        parallax = gallery.Gallery.objects.get(name='Parallax')
        for c, i in enumerate(parallax.images.all()):
            i.description = descriptions[c]
            i.save()

        parallax.limit = 3
        parallax.save()

        articles = gallery.Gallery.objects.get(name='Articles')
        articles.limit = 1024
        articles.save()

        stock = gallery.Gallery.objects.get(name='Stock')
        stock.limit = 32
        stock.save()
