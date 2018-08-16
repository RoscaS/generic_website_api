from rest_framework import serializers
from .models import Category, Item

class ItemSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    category = serializers.SlugRelatedField(slug_field='slug', queryset=Category.objects.all())

    class Meta:
        model = Item
        fields = (
            'id',
            'name',
            'price',
            'position',
            'category',
            'description',
            'image',
        )


class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        fields = (
            'slug',
            'name',
            'description',
            'position',
            'items',
        )
