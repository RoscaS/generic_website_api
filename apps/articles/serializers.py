from rest_framework import serializers
from .models import Category, Article

class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='slug', queryset=Category.objects.all())

    class Meta:
        model = Article
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
    articles = ArticleSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        fields = (
            'id',
            'slug',
            'name',
            'description',
            'position',
            'articles',
        )
