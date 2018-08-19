import os, shutil

from rest_framework import viewsets

from apps.gallery.models import Gallery, Image
from django.conf import settings
from .models import PresentationSection, HeroSection, EventsSection, \
    ContactSection, MainOptions, Message, ReviewSection, PromoSection, Texts
from .serializers import PresentationSerializer, HeroSerializer, \
    EventsSerializer, ContactSerializer, MainOptionsSerializer, \
    MessageSerializer, ReviewSerializer, PromoSerializer, TextsSerializer


# http_method_names = ['get', 'post', 'put', 'patch', 'delete']


class MainOptionsViewSet(viewsets.ModelViewSet):
    queryset = MainOptions.objects.all()
    serializer_class = MainOptionsSerializer
    http_method_names = ['get', 'patch']
    # permission_classes = (permissions.IsAdminUser, )


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    http_method_names = ['get', 'post', 'patch']
    # permission_classes = (permissions.IsAdminUser, )




class PromoViewSet(viewsets.ModelViewSet):
    queryset = PromoSection.objects.all()
    serializer_class = PromoSerializer
    http_method_names = ['get', 'put']
    # permission_classes = (permissions.IsAdminUser, )

    def update(self, request, pk=None):
        print('\n\nPROMO\n\n')
        gallery_path = os.path.join(settings.MEDIA_ROOT,'galleries')
        _temp_images = os.listdir(os.path.join(gallery_path, '_temp'))
        if _temp_images:
            image = Image.objects.filter(gallery__name='_temp').first()
            shutil.move(f"{gallery_path}/_temp/{_temp_images[0]}",
                        f"{gallery_path}/misc/action.jpg")
            image.image = f"{gallery_path}/misc/action.jpg"
            image.gallery = Gallery.objects.get(name='misc')
            image.save()
        return super().update(request)


class PresentationViewSet(viewsets.ModelViewSet):

    queryset = PresentationSection.objects.all()
    serializer_class = PresentationSerializer
    http_method_names = ['get', 'put']
    # permission_classes = (permissions.IsAdminUser, )

    def update(self, request, pk=None):
        print('\n\nPRESENTATION\n\n')
        # gallery_path = f'{settings.BASE_DIR}/media/galleries'

        gallery_path = os.path.join(settings.MEDIA_ROOT,'galleries')
        _temp_images = os.listdir(os.path.join(gallery_path, '_temp'))
        if _temp_images:
            image = Image.objects.filter(gallery__name='_temp').first()
            shutil.move(f"{gallery_path}/_temp/{_temp_images[0]}",
                        f"{gallery_path}/misc/presentation.jpg")
            image.image = f"{gallery_path}/misc/presentation.jpg"
            image.gallery = Gallery.objects.get(name='misc')
            image.save()
            print(f"{gallery_path}/misc/presentation.jpg")
        return super().update(request)

class HeroViewSet(viewsets.ModelViewSet):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSerializer
    http_method_names = ['get', 'put']
    # permission_classes = (permissions.IsAdminUser, )


class EventsViewSet(viewsets.ModelViewSet):
    queryset = EventsSection.objects.all()
    serializer_class = EventsSerializer
    http_method_names = ['get', 'put']
    # permission_classes = (permissions.IsAdminUser, )


class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactSection.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ['get', 'put']
    # permission_classes = (permissions.IsAdminUser, )


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = ReviewSection.objects.all()
    serializer_class = ReviewSerializer
    http_method_names = ['get', 'put']
    # permission_classes = (permissions.IsAdminUser, )


class TextsViewSet(viewsets.ModelViewSet):
    queryset = Texts.objects.all()
    serializer_class = TextsSerializer
    http_method_names = ['get']
    # permission_classes = (permissions.IsAdminUser, )



