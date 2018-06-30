import forgery_py

from django.db import models
from django.conf import settings
from apps.gallery.models import Image

DATA = settings.WEBSITE_DATA

def sentences(n):
    return forgery_py.lorem_ipsum.sentences(n).capitalize()+'.'


class Presentation(models.Model):
    title = models.CharField(max_length=200, null=False,
                             default=DATA['DESCRIPTION'] or forgery_py.lorem_ipsum.sentence())
    sub_title = models.TextField(max_length=200, null=False, default=sentences(1))
    text1 = models.TextField(max_length=4000, default=sentences(10))
    text2 = models.TextField(max_length=4000, default=sentences(13))
    image = models.ForeignKey(Image, related_name=None, on_delete=models.CASCADE)
