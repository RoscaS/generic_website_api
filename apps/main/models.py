import forgery_py
import requests
from random import randint

from django.db import models
from django.conf import settings

from apps.gallery.models import Image

DATA = settings.WEBSITE_DATA

def sentences(n):
    return forgery_py.lorem_ipsum.sentences(n).capitalize()

def words(n):
    w = forgery_py.lorem_ipsum.words(n).capitalize()
    return w if n <= 2 else w + '.'


class MainOptions(models.Model):
    # project_name = models.CharField(max_length=15, null=False, default=DATA['PROJECT_NAME'] or '')
    # name = models.CharField(max_length=15, null=False, default=DATA['NAME'] or '')
    # name_add = models.CharField(max_length=9, null=False, default=DATA['NAME_ADD'] or '')
    # description = models.CharField(max_length=30, null=False, default=DATA['DESCRIPTION'] or '')
    # oppening = models.CharField(max_length=4, null=False, default=DATA['OUVERTURE'] or '')
    # adress = models.CharField(max_length=30, null=False, default=DATA['ADRESSE'] or '')
    # city = models.CharField(max_length=30, null=True, default=DATA['VILLE'] or '', blank=True)
    # post_code = models.CharField(max_length=4, null=True, default=DATA['CODE_POSTAL'] or '', blank=True)
    # phone = models.CharField(max_length=30, null=True, default=DATA['TELEPHONE'] or '', blank=True)
    # mail = models.EmailField(max_length=30, null=True, default=DATA['EMAIL'] or '', blank=True)
    # facebook = models.CharField(max_length=1000, null=True, default=DATA['FACEBOOK'] or '', blank=True)
    # tripadvisor = models.CharField(max_length=1000, null=True, default=DATA['TRIPADVISOR'] or '', blank=True)
    # google = models.CharField(max_length=1000, null=True, default=DATA['GOOGLE'] or '', blank=True)
    # twitter = models.CharField(max_length=1000, null=True, default=DATA['TWITTER'] or '', blank=True)
    # instagram = models.CharField(max_length=1000, null=True, default=DATA['INSTAGRAM'] or '', blank=True)
    # linkedin = models.CharField(max_length=1000, null=True, default=DATA['LINKEDIN'] or '', blank=True)
    # snapchat = models.CharField(max_length=1000, null=True, default=DATA['SNAPCHAT'] or '', blank=True)
    mapBox = models.CharField(max_length=1000, null=True, default=DATA['MAPBOX'] or '', blank=True)



class SiteInformations(models.Model):
    name = models.CharField(max_length=25, null=False, default=DATA['NAME'] or '')
    name_add = models.CharField(max_length=15, null=False, default=DATA['NAME_ADD'] or '')
    oppening = models.CharField(max_length=4, null=False, default=DATA['OUVERTURE'] or '')
    adress = models.CharField(max_length=30, null=False, default=DATA['ADRESSE'] or '')
    city = models.CharField(max_length=30, null=False, default=DATA['VILLE'] or '')
    post_code = models.CharField(max_length=8, null=False, default=DATA['CODE_POSTAL'] or '')
    phone = models.CharField(max_length=30, null=True, default=DATA['TELEPHONE'] or '', blank=True)
    mail = models.EmailField(max_length=30, null=True, default=DATA['EMAIL'] or '', blank=True)


class SiteContact(models.Model):
    facebook = models.CharField(max_length=1000, null=True, default=DATA['FACEBOOK'] or '', blank=True)
    tripadvisor = models.CharField(max_length=1000, null=True, default=DATA['TRIPADVISOR'] or '', blank=True)
    google = models.CharField(max_length=1000, null=True, default=DATA['GOOGLE'] or '', blank=True)
    twitter = models.CharField(max_length=1000, null=True, default=DATA['TWITTER'] or '', blank=True)
    instagram = models.CharField(max_length=1000, null=True, default=DATA['INSTAGRAM'] or '', blank=True)
    linkedin = models.CharField(max_length=1000, null=True, default=DATA['LINKEDIN'] or '', blank=True)
    snapchat = models.CharField(max_length=1000, null=True, default=DATA['SNAPCHAT'] or '', blank=True)


class AuthTest(models.Model):
    name = models.CharField(default='AuthTest', max_length=15)
    title = models.CharField(max_length=35, null=False, default='AuthTest view')
    text = models.CharField(max_length=800, null=False, default=sentences(4))
    # image = models.ForeignKey(Image, related_name=None, on_delete=models.CASCADE, null=True)



class Message(models.Model):
    name = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=30, null=False)
    message = models.TextField(max_length=3000, null=False)
    date = models.DateTimeField(auto_now_add=True)
    is_new = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date']


class PromoSection(models.Model):
    name = models.CharField(default='Promo', max_length=15)
    title = models.CharField(max_length=35, null=False, default='A title')
    text = models.CharField(max_length=800, null=False, default=sentences(4))
    # image = models.ForeignKey(Image, related_name=None, on_delete=models.CASCADE, null=True)


class PresentationSection(models.Model):
    name = models.CharField(default='Presentation', max_length=15)
    title = models.CharField(max_length=35, null=False, default=DATA['DESCRIPTION'] or sentences(1))
    sub_title = models.TextField(max_length=200, null=False, default=sentences(randint(1,3)))
    text1 = models.TextField(max_length=800, default=sentences(8))
    text2 = models.TextField(max_length=800, default=sentences(9))
    # image = models.ForeignKey(Image, related_name=None, on_delete=models.CASCADE)


class HeroSection(models.Model):
    name = models.CharField(default='Hero', max_length=15)
    icon1 = models.CharField(max_length=20, null=False, default="fab fa-cloudversify")
    icon2 = models.CharField(max_length=20, null=False, default="far fa-paint-brush")
    icon3 = models.CharField(max_length=20, null=False, default="far fa-compass")
    title1 = models.CharField(max_length=20, null=False, default=words(2))
    title2 = models.CharField(max_length=20, null=False, default=words(2))
    title3 = models.CharField(max_length=20, null=False, default=words(2))
    text1 = models.CharField(max_length=200, null=False, default=sentences(2))
    text2 = models.CharField(max_length=200, null=False, default=sentences(2))
    text3 = models.CharField(max_length=200, null=False, default=sentences(2))


class ArticlesSection(models.Model):
    name = models.CharField(default='Articles', max_length=15)
    header = models.CharField(max_length=30, null=False, default='Articles')
    title = models.CharField(max_length=35, null=False, default='Articles')
    sub_title = models.TextField(max_length=200, null=False, default=sentences(randint(1,3)))


class EventsSection(models.Model):
    name = models.CharField(default='Events', max_length=15)
    header = models.CharField(max_length=30, null=False, default='Galerie')
    title = models.CharField(max_length=35, null=False, default='Derniers événements')
    sub_title = models.TextField(max_length=200, null=False, default=sentences(randint(1,3)))


class ContactSection(models.Model):
    name = models.CharField(default='Contact', max_length=15)
    header = models.CharField(max_length=30, null=False, default='Contact')
    title = models.CharField(max_length=35, null=False, default='Où nous trouver')
    sub_title = models.TextField(max_length=200, null=False, default="N'hésitez pas à nous contacter...")
    sub_title2 = models.TextField(max_length=200, null=False, default='... en nous laissant un message...')
    sub_title3 = models.TextField(max_length=200, null=False, default='... ou en passant directement nous voir:')


class ReviewSection(models.Model):
    name = models.CharField(default='Review', max_length=15)
    title = models.CharField(max_length=35, null=False, default='Google Review')
    sub_title = models.CharField(max_length=200, null=False, default='Ce que disent les gens de nous')
    g_api = models.CharField(max_length=1000, null=True, default=DATA['GOOGLE_API'] or '', blank=True)
    g_place_id = models.CharField(max_length=1000, null=True, default=DATA['GOOGLE_PLACE_ID'] or '', blank=True)
    g_review_all_url = models.CharField(max_length=1000, null=True, default=DATA['GOOGLE_REVIEW_LINK_ALL'] or '', blank=True)
    g_review_new_url = models.CharField(max_length=1000, null=True, default=DATA['GOOGLE_REVIEW_LINK_WRITE'] or '', blank=True)

    @property
    def reviews(self):
        response = requests.get(DATA['GOOGLE_PLACE'])
        d = response.json()['result']
        overall = d['rating']
        reviews_lst = d['reviews']
        return ({'overall': overall, 'reviews': reviews_lst})

