import forgery_py

from django.db import models
from django.conf import settings
from django.core.mail import send_mail

from apps.gallery.models import Image

DATA = settings.WEBSITE_DATA

def sentences(n):
    return forgery_py.lorem_ipsum.sentences(n).capitalize()

def words(n):
    w = forgery_py.lorem_ipsum.words(n).capitalize()
    return w if n <= 2 else w + '.'


class PresentationSection(models.Model):
    title = models.CharField(max_length=200, null=False,
                             default=DATA['DESCRIPTION'] or sentences(1))
    sub_title = models.TextField(max_length=200, null=False, default=sentences(1))
    text1 = models.TextField(max_length=4000, default=sentences(10))
    text2 = models.TextField(max_length=4000, default=sentences(13))
    image = models.ForeignKey(Image, related_name=None, on_delete=models.CASCADE)


class HeroSection(models.Model):
    icon1 = models.CharField(max_length=20, null=False, default="fab fa-cloudversify")
    icon2 = models.CharField(max_length=20, null=False, default="far fa-paint-brush")
    icon3 = models.CharField(max_length=20, null=False, default="far fa-compass")
    title1 = models.CharField(max_length=20, null=False, default=words(2))
    title2 = models.CharField(max_length=20, null=False, default=words(2))
    title3 = models.CharField(max_length=20, null=False, default=words(2))
    text1 = models.CharField(max_length=1000, null=False, default=sentences(3))
    text2 = models.CharField(max_length=1000, null=False, default=sentences(3))
    text3 = models.CharField(max_length=1000, null=False, default=sentences(3))


class GallerySection(models.Model):
    header = models.CharField(max_length=30, null=False, default='Galerie')
    title = models.CharField(max_length=200, null=False, default='Derniers événements')
    sub_title = models.TextField(max_length=200, null=False, default=sentences(1))


class ContactSection(models.Model):
    header = models.CharField(max_length=30, null=False, default='Contact')
    title = models.CharField(max_length=200, null=False, default='Où nous trouver')
    sub_title = models.TextField(max_length=200, null=False, default="N'hésitez pas à nous contacter...")
    sub_title2 = models.TextField(max_length=200, null=False, default='... en nous laissant un message...')
    sub_title3 = models.TextField(max_length=200, null=False, default='... ou en passant directement nous voir.')


class MainOptions(models.Model):
    name = models.CharField(max_length=15, null=False, default=DATA['NAME'] or '', help_text='Nom du commerce.')
    name_add = models.CharField(max_length=9, null=False, default=DATA['NAME_ADD'] or '', help_text='type de commerce.')
    description = models.CharField(max_length=30, null=False, default=DATA['DESCRIPTION'] or '', help_text='Très brève description.')
    oppening = models.CharField(max_length=4, null=False, default=DATA['OUVERTURE'] or '', help_text='Année d\'ouverture.')
    adress = models.CharField(max_length=30, null=False, default=DATA['ADRESSE'] or '', help_text='numéro + rue (12 rue des champs)')
    city = models.CharField(max_length=30, null=True, default=DATA['VILLE'] or '', blank=True)
    post_code = models.CharField(max_length=4, null=True, default=DATA['CODE_POSTAL'] or '', blank=True)
    phone = models.CharField(max_length=30, null=True, default=DATA['TELEPHONE'] or '', blank=True)
    mail = models.EmailField(max_length=30, null=True, default=DATA['EMAIL'] or '', blank=True)
    facebook = models.CharField(max_length=1000, null=True, default=DATA['FACEBOOK'] or '', blank=True)
    tripadvisor = models.CharField(max_length=1000, null=True, default=DATA['TRIPADVISOR'] or '', blank=True)
    google = models.CharField(max_length=1000, null=True, default=DATA['GOOGLE'] or '', blank=True)
    twitter = models.CharField(max_length=1000, null=True, default=DATA['TWITTER'] or '', blank=True)
    instagram = models.CharField(max_length=1000, null=True, default=DATA['INSTAGRAM'] or '', blank=True)
    linkedin = models.CharField(max_length=1000, null=True, default=DATA['LINKEDIN'] or '', blank=True)
    snapchat = models.CharField(max_length=1000, null=True, default=DATA['SNAPCHAT'] or '', blank=True)


class Message(models.Model):
    name = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=30, null=False)
    message = models.TextField(max_length=3000, null=False)
    date = models.DateTimeField(auto_now_add=True)
    is_new = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date']
