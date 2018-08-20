import os, shutil, json
from pathlib import Path
from random import randint

from rest_framework import viewsets
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
    http_method_names = ['get', 'post']

    @action(methods=['post'], detail=False)
    def get_placeholder(self, request, pk=None):
        gallery = Gallery.objects.get(name=request.data['gallery'])
        dest = Path(os.path.join(media, 'galleries', 'placeholders'))
        if not Path.exists(dest):
            os.mkdir(dest)

        name = f'placeholder_{request.data["gallery"]}.jpg'
        file = os.path.join(dest, name)
        shutil.copy(f'{static}/placeholder.jpg', file)
        img = Image.objects.create(
            image=f'galleries/placeholders/{name}',
            gallery=gallery,
            name=name
        )
        img.save()
        serialized = ImageSerializer(img)
        return Response(serialized.data)


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser)
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    # def create(self, request):
    #     images = Gallery.objects.get(name='_temp').images.all()
    #     for image in images:
    #         image.delete()
    #     return super().create(request)

    def partial_update(self, request, pk=None):
        data = request.data
        image = Image.objects.get(id=data['id'])
        if image.gallery.name != data['gallery']:
            print(f"FRONT\tid: {data['id']}\tgal: {data['gallery']}\nBACK\tid: {image.id}\tgal: {image.gallery.name}\n\n")
            image.gallery = Gallery.objects.get(name=data['gallery'])

            image.save()
        return super().partial_update(request, pk)
