from django.db import models
from apps.gallery.models import Gallery

class Section(models.Model):
    slug = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200, null=False)
    title = models.CharField(max_length=35, null=False)
    sub_title = models.TextField(max_length=200, null=True, blank=True)
    text1 = models.TextField(max_length=800, null=True, blank=True)
    text2 = models.TextField(max_length=800, null=True, blank=True)
    gallery = models.ForeignKey(Gallery, related_name='section', null=True, blank=True, on_delete=models.CASCADE)


# class GenericSection(models.Model):
#     name = models.CharField(max_length=15, null=False, blank=False)
#     title = models.CharField(max_length=35, null=False, blank=False)
#     sub_title = models.TextField(max_length=200, null=False, blank=False)
#     text1 = models.TextField(max_length=800, blank=False)
#     text2 = models.TextField(max_length=800, blank=False)

    # @property
    # def section(self):
    #     return Section.objects.get(name=self.name).
