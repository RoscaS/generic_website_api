from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.gallery.models import Gallery
from .serializers import SectionSerializer
from .models import Section


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    lookup_field = 'slug'
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def update(self, request, *args, **kwargs):
        name = ''.join([i.capitalize() for i in request.data['title'].split()])
        gallery = Gallery.objects.get(**kwargs)
        gallery.name = name
        gallery.slug = name
        gallery.save()
        request.data['name'] = name
        request.data['slug'] = name
        return super().update(request, *args, **kwargs)

