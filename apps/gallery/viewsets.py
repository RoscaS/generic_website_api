import os, shutil
from pathlib import Path

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from rest_framework.response import Response
from django.conf import settings
from .models import Gallery, Image
from .serializers import ImageSerializer, GallerySerializer

static = settings.STATIC_ROOT
media = settings.MEDIA_ROOT

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    lookup_field = 'slug'
    http_method_names = ['get', 'post', 'delete']
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @action(methods=['post'], detail=False)
    def get_placeholder(self, request, pk=None):
        gallery = Gallery.objects.get(name=request.data['gallery'])
        return Response(ImageSerializer(gallery.set_placeholder()).data)


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser)
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def partial_update(self, request, pk=None):
        data = request.data
        image = Image.objects.get(id=data['id'])
        if image.gallery.name != data['gallery']:
            image.gallery = Gallery.objects.get(name=data['gallery'])
            image.save()
        return super().partial_update(request, pk)
