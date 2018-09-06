from . import viewsets

routeList = (
    (r'authtest', viewsets.AuthTestViewSet),
    (r'presentation', viewsets.PresentationViewSet),
    (r'hero', viewsets.HeroViewSet),
    (r'article', viewsets.ArticlesViewSet),

)
