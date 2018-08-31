from rest_framework import serializers
from .models import Gallery, Image


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    gallery = serializers.SlugRelatedField(slug_field='slug', queryset=Gallery.objects.all())

    class Meta:
        model = Image
        fields = (
            'id',
            'name',
            'position',
            'gallery',
            'description',
            'image'
        )
        # depth = 1


class GallerySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Gallery
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        fields = (
            'id',
            'name',
            'description',
            'url',
            'images',
            'limit'
        )


'''
curl \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTM1NTgzMjAwLCJqdGkiOiI0ZDBkMTgyMjMzOWQ0ODZiOTAxNDAyZWNmNjVkNjQ5NSIsInVzZXJfaWQiOjF9.Fr8YfR_MbZ7ERFbgvB_05G9fXdVue4-6bN4Numd6AIU" \
  http://localhost:8000/api/authtest/
'''
