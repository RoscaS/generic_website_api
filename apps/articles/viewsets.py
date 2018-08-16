from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    http_method_names = ['get', 'post']


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    parser_classes = (MultiPartParser, FormParser)
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
