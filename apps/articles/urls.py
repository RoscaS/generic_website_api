from . import viewsets

routeList = (
    (r'categories', viewsets.CategoryViewSet),
    (r'articles', viewsets.ArticleViewSet),
)
