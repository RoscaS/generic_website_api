from rest_framework import viewsets
from .models import Presentation, Hero
from .serializers import PresentationSerializer, HeroSerializer


class PresentationViewSet(viewsets.ModelViewSet):
    queryset = Presentation.objects.all()
    serializer_class = PresentationSerializer
    lookup_field = 'slug'

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    lookup_field = 'slug'
