from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import SectionSerializer
from .models import Section


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    lookup_field = 'slug'
    http_method_names = ['get', 'post', 'delete']
    permission_classes = (IsAuthenticatedOrReadOnly,)

# class GenericSectionViewSet(viewsets.ModelViewSet):
#     queryset = GenericSection.objects.all()
#     serializer_class = GenericSectionSerializer
#     lookup_field = 'slug'
#     http_method_names = ['get', 'post', 'delete']
#     permission_classes = (IsAuthenticatedOrReadOnly,)

