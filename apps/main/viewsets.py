from rest_framework import viewsets, permissions

from .models import PresentationSection, HeroSection, EventsSection, \
    ContactSection, MainOptions, Message, ReviewSection, PromoSection, \
    ArticlesSection
from .serializers import PresentationSerializer, HeroSerializer, \
    EventsSerializer, ContactSerializer, MainOptionsSerializer, \
    MessageSerializer, ReviewSerializer, PromoSerializer, \
    ArticlesSerializer


# http_method_names = ['get', 'post', 'put', 'patch', 'delete']


class MainOptionsViewSet(viewsets.ModelViewSet):
    queryset = MainOptions.objects.all()
    serializer_class = MainOptionsSerializer
    http_method_names = ['get', 'patch']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    http_method_names = ['get', 'post', 'patch']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class PromoViewSet(viewsets.ModelViewSet):
    queryset = PromoSection.objects.all()
    serializer_class = PromoSerializer
    http_method_names = ['get', 'put']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class PresentationViewSet(viewsets.ModelViewSet):
    queryset = PresentationSection.objects.all()
    serializer_class = PresentationSerializer
    http_method_names = ['get', 'put']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class HeroViewSet(viewsets.ModelViewSet):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSerializer
    http_method_names = ['get', 'put']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class EventsViewSet(viewsets.ModelViewSet):
    queryset = EventsSection.objects.all()
    serializer_class = EventsSerializer
    http_method_names = ['get', 'put']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = ArticlesSection.objects.all()
    serializer_class = ArticlesSerializer
    http_method_names = ['get', 'put']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactSection.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ['get', 'put']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = ReviewSection.objects.all()
    serializer_class = ReviewSerializer
    http_method_names = ['get', 'put']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
