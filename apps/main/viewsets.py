from rest_framework import viewsets
from .models import Presentation
from .serializers import PresentationSerializer


class PresentationViewSet(viewsets.ModelViewSet):
    queryset = Presentation.objects.all()
    serializer_class = PresentationSerializer
    lookup_field = 'slug'

