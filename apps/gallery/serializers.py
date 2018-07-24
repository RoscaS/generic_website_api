from rest_framework import serializers
from .models import Gallery, Image

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    # gallery_name = serializers.ReadOnlyField(source='gallery.name')
    gallery = serializers.SlugRelatedField(slug_field='slug', queryset=Gallery.objects.all())

    class Meta:
        model = Image
        fields = ('id', 'position', 'gallery', 'description', 'image')
        # fields = ('image', 'id', 'gallery', 'gallery_name', 'description')
        # depth = 1


class GallerySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = ('id', 'name', 'description', 'url', 'images')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
