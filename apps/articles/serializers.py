from rest_framework import serializers
from .models import Category, Item

class ItemSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    category = serializers.SlugRelatedField(slug_field='slug', queryset=Category.objects.all())

    class Meta:
        model = Item
        fields = '__ALL__'


class CategorySerializer(serializers.ModelSerializer):
    articles = ItemSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__ALL__'
