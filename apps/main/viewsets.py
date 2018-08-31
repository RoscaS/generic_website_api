from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

from .models import (
    PresentationSection,
    HeroSection,
    EventsSection,
    ContactSection,
    MainOptions,
    Message,
    ReviewSection,
    PromoSection,
    ArticlesSection,
    AuthTest,
)
from .serializers import (
    PresentationSerializer,
    HeroSerializer,
    EventsSerializer,
    ContactSerializer,
    MainOptionsSerializer,
    MessageSerializer,
    ReviewSerializer,
    PromoSerializer,
    ArticlesSerializer,
    AuthTestSerializer,
)


# http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class AuthTestViewSet(viewsets.ModelViewSet):
    queryset = AuthTest.objects.all()
    serializer_class = AuthTestSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = (is_admin_or_read_only,)


class MainOptionsViewSet(viewsets.ModelViewSet):
    queryset = MainOptions.objects.all()
    serializer_class = MainOptionsSerializer
    http_method_names = ['get', 'patch']
    # authentication_class = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = (is_admin_or_read_only, )


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    http_method_names = ['get', 'post', 'patch']
    # authentication_class = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = (is_admin_or_read_only, )


class PromoViewSet(viewsets.ModelViewSet):
    queryset = PromoSection.objects.all()
    serializer_class = PromoSerializer
    http_method_names = ['get', 'put']
    # authentication_class = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = (is_admin_or_read_only, )


class PresentationViewSet(viewsets.ModelViewSet):
    queryset = PresentationSection.objects.all()
    serializer_class = PresentationSerializer
    http_method_names = ['get', 'put']
    # authentication_class = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = (is_admin_or_read_only, )


class HeroViewSet(viewsets.ModelViewSet):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSerializer
    http_method_names = ['get', 'put']
    # authentication_class = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = (is_admin_or_read_only, )


class EventsViewSet(viewsets.ModelViewSet):
    queryset = EventsSection.objects.all()
    serializer_class = EventsSerializer
    http_method_names = ['get', 'put']
    # authentication_class = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = (is_admin_or_read_only, )


class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = ArticlesSection.objects.all()
    serializer_class = ArticlesSerializer
    http_method_names = ['get', 'put']
    # authentication_class = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = (is_admin_or_read_only, )


class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactSection.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ['get', 'put']
    # authentication_class = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = (is_admin_or_read_only, )


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = ReviewSection.objects.all()
    serializer_class = ReviewSerializer
    http_method_names = ['get', 'put']
    # authentication_class = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = (is_admin_or_read_only, )
