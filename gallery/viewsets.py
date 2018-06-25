from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Gallery, Image
from .serializers import ImageSerializer, GallerySerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'galleries': reverse('gallery-list', request=request, format=format),
        'images': reverse('image-list', request=request, format=format)
    })

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
