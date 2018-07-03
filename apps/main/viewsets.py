from rest_framework import viewsets
from .models import PresentationSection, HeroSection, GallerySection, \
    ContactSection, MainOptions, Message
from .serializers import PresentationSerializer, HeroSerializer, \
    GallerySerializer, ContactSerializer, MainOptionsSerializer, MessageSerializer


# http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class PresentationViewSet(viewsets.ModelViewSet):
    queryset = PresentationSection.objects.all()
    serializer_class = PresentationSerializer
    http_method_names = ['get', 'patch']


class HeroViewSet(viewsets.ModelViewSet):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSerializer
    http_method_names = ['get', 'patch']


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = GallerySection.objects.all()
    serializer_class = GallerySerializer
    http_method_names = ['get', 'patch']


class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactSection.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ['get', 'patch']


class MainOptionsViewSet(viewsets.ModelViewSet):
    queryset = MainOptions.objects.all()
    serializer_class = MainOptionsSerializer
    http_method_names = ['get', 'patch']


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    http_method_names = ['get', 'post', 'patch']


