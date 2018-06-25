from rest_framework import serializers
from .models import Gallery, Image

# class ImageSerializer(serializers.HyperlinkedIdentityField):
class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    gallery = serializers.HyperlinkedRelatedField(view_name='gallery-detail', read_only=True)
    gallery_name = serializers.ReadOnlyField(source='gallery.name')

    class Meta:
        model = Image
        fields = ('image', 'gallery', 'gallery_name')


# class GallerySerializer(serializers.HyperlinkedIdentityField):
class GallerySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = ('name', 'description', 'images')
