from rest_framework import viewsets
from rest_framework import permissions
from .models import PresentationSection, HeroSection, GallerySection, \
    ContactSection, MainOptions, Message, ReviewSection
from .serializers import PresentationSerializer, HeroSerializer, \
    GallerySerializer, ContactSerializer, MainOptionsSerializer, \
    MessageSerializer, ReviewSerializer


# http_method_names = ['get', 'post', 'put', 'patch', 'delete']


class MainOptionsViewSet(viewsets.ModelViewSet):
    queryset = MainOptions.objects.all()
    serializer_class = MainOptionsSerializer
    http_method_names = ['get', 'patch']
    permission_classes = (permissions.IsAdminUser, )


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    http_method_names = ['get', 'post', 'patch']
    permission_classes = (permissions.IsAdminUser, )



class PresentationViewSet(viewsets.ModelViewSet):
    queryset = PresentationSection.objects.all()
    serializer_class = PresentationSerializer
    http_method_names = ['get', 'patch']
    permission_classes = (permissions.IsAdminUser, )



class HeroViewSet(viewsets.ModelViewSet):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSerializer
    http_method_names = ['get', 'patch']
    permission_classes = (permissions.IsAdminUser, )



class GalleryViewSet(viewsets.ModelViewSet):
    queryset = GallerySection.objects.all()
    serializer_class = GallerySerializer
    http_method_names = ['get', 'patch']
    permission_classes = (permissions.IsAdminUser, )



class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactSection.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ['get', 'patch']
    permission_classes = (permissions.IsAdminUser, )



class ReviewViewSet(viewsets.ModelViewSet):
    queryset = ReviewSection.objects.all()
    serializer_class = ReviewSerializer
    http_method_names = ['get', 'patch']
    permission_classes = (permissions.IsAdminUser, )




