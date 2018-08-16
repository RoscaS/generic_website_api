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
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']


    def create(self, request):
        images = Gallery.objects.get(name='_temp').images.all()
        for image in images:
            image.delete()
        return super().create(request)

    def partial_update(self, request, pk=None):
        data = request.data
        image = Image.objects.get(id=data['id'])
        if image.gallery.name != data['gallery']:
            print(f"FRONT\tid: {data['id']}\tgal: {data['gallery']}\nBACK\tid: {image.id}\tgal: {image.gallery.name}\n\n")
            image.gallery = Gallery.objects.get(name=data['gallery'])

            image.save()
        return super().partial_update(request, pk)
