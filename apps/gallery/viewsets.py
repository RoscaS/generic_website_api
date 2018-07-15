from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Gallery, Image
from .serializers import ImageSerializer, GallerySerializer


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    lookup_field = 'slug'
    http_method_names = ['get']


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request):
        images = Gallery.objects.get(name='_temp').images.all()
        for image in images:
            image.delete()
        return super().create(request)
