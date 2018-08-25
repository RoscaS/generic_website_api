from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from apps.gallery.models import Image, Gallery
from .models import Category, Article
from .serializers import CategorySerializer, ArticleSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    parser_classes = (MultiPartParser, FormParser)
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def partial_update(self, request, pk=None):
        data = request.data
        article = Article.objects.get(id=data['id'])
        if article.category.name != data['category']:
            article.category = Category.objects.get(name=data['category'])
            article.save()
        return super().partial_update(request, pk)


    # @action(methods=['post'], detail=True)
    # def image_preview(self, request, pk=None):
    #     data = request.data
    #     gallery = Gallery.objects.get(name='Stock')
    #     image = Image.objects.create(
    #         name='articles_temp_image',
    #         gallery=gallery,
    #         image=data['image']
    #     )
    #     return Response({'url': image.image}, {'id': image.id})
    #
    # @action(methods=['post'], detail=True)
    # def set_image(self, request, pk=None):
    #     data = request.data
    #     article = Article.objects.get(id=data['article_id'])
    #     image = Image.objects.get(id=data['image_id'])
    #     article.image = image
    #     article.save()
    #     return image
    #
    #     return Response({'url': image.image}, {'id': image.id})
    #
    # def create(self, request):
    #     data = request.data
    #     gallery = Gallery.objects.get(name='Articles')
    #     image = Image.objects.get(id=data['image_id'])
    #     image = Image.objects.create(
    #         name=data['name'],
    #         gallery=gallery,
    #         image=data['image']
    #     )
    #     request.data['image'] = image
    #     return super().create(request)
