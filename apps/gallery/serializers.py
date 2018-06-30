from rest_framework import serializers
from .models import Gallery, Image

# class ImageSerializer(serializers.HyperlinkedIdentityField):
class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    # gallery = serializers.HyperlinkedRelatedField(view_name='gallery-detail', read_only=True)
    gallery_name = serializers.ReadOnlyField(source='gallery.name')
    gallery_id = serializers.ReadOnlyField(source='gallery.id')

    class Meta:
        model = Image
        fields = ('image', 'gallery_id', 'gallery_name', 'description')


# class GallerySerializer(serializers.HyperlinkedIdentityField):
class GallerySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = ('url', 'slug', 'name', 'description', 'images')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
