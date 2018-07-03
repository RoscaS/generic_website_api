from rest_framework import viewsets
from .models import PresentationSection, HeroSection, GallerySection, \
    ContactSection, MainOptions
from .serializers import PresentationSerializer, HeroSerializer, \
    GallerySerializer, ContactSerializer, MainOptionsSerializer


class PresentationViewSet(viewsets.ModelViewSet):
    queryset = PresentationSection.objects.all()
    serializer_class = PresentationSerializer
    lookup_field = 'slug'


class HeroViewSet(viewsets.ModelViewSet):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSerializer
    lookup_field = 'slug'


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = GallerySection.objects.all()
    serializer_class = GallerySerializer
    lookup_field = 'slug'


class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactSection.objects.all()
    serializer_class = ContactSerializer
    lookup_field = 'slug'


class MainOptionsViewSet(viewsets.ModelViewSet):
    queryset = MainOptions.objects.all()
    serializer_class = MainOptionsSerializer
    lookup_field = 'slug'
