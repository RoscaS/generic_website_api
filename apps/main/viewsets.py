from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

from .models import (
    PresentationSection,
    HeroSection,
    EventsSection,
    ContactSection,
    SiteOptions,
    Message,
    ReviewSection,
    PromoSection,
    ArticlesSection,
    AuthTest,
    SiteInformations,
    SiteContact,
)
from .serializers import (
    PresentationSerializer,
    HeroSerializer,
    EventsSerializer,
    ContactSerializer,
    SiteOptionsSerializer,
    MessageSerializer,
    ReviewSerializer,
    PromoSerializer,
    ArticlesSerializer,
    AuthTestSerializer,
    SiteInformationsSerializer,
    SiteContactSerializer
)

# http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class AuthTestViewSet(viewsets.ModelViewSet):
    queryset = AuthTest.objects.all()
    serializer_class = AuthTestSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = (IsAuthenticatedOrReadOnly,)


class SiteOptionsViewSet(viewsets.ModelViewSet):
    queryset = SiteOptions.objects.all()
    serializer_class = SiteOptionsSerializer
    http_method_names = ['get', 'put']
    permission_classes = (IsAuthenticatedOrReadOnly,)


class SiteInformationsViewSet(viewsets.ModelViewSet):
    queryset = SiteInformations.objects.all()
    serializer_class = SiteInformationsSerializer
    http_method_names = ['get', 'put']
    permission_classes = (IsAuthenticatedOrReadOnly,)


class SiteContactViewSet(viewsets.ModelViewSet):
    queryset = SiteContact.objects.all()
    serializer_class = SiteContactSerializer
    http_method_names = ['get', 'put']
    permission_classes = (IsAuthenticatedOrReadOnly,)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    http_method_names = ['get', 'post', 'patch']
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PromoViewSet(viewsets.ModelViewSet):
    queryset = PromoSection.objects.all()
    serializer_class = PromoSerializer
    http_method_names = ['get', 'put']
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PresentationViewSet(viewsets.ModelViewSet):
    queryset = PresentationSection.objects.all()
    serializer_class = PresentationSerializer
    http_method_names = ['get', 'put']
    permission_classes = (IsAuthenticatedOrReadOnly,)


class HeroViewSet(viewsets.ModelViewSet):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSerializer
    http_method_names = ['get', 'put']
    permission_classes = (IsAuthenticatedOrReadOnly,)


class EventsViewSet(viewsets.ModelViewSet):
    queryset = EventsSection.objects.all()
    serializer_class = EventsSerializer
    http_method_names = ['get', 'put']
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = ArticlesSection.objects.all()
    serializer_class = ArticlesSerializer
    http_method_names = ['get', 'put']
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactSection.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ['get', 'put']
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = ReviewSection.objects.all()
    serializer_class = ReviewSerializer
    http_method_names = ['get', 'put']
    permission_classes = (IsAuthenticatedOrReadOnly,)
