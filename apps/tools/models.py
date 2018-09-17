from django.db import models
from apps.gallery.models import Gallery

class GrecaptchaToken(models.Model):
    token = models.CharField(max_length=2048)
