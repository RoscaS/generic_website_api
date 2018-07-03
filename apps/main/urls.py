from . import viewsets

routeList = (
    (r'presentation', viewsets.PresentationViewSet),
    (r'hero', viewsets.HeroViewSet),
    (r'gallery', viewsets.GalleryViewSet),
    (r'contact', viewsets.ContactViewSet),
    (r'options', viewsets.MainOptionsViewSet),
    (r'message', viewsets.MessageViewSet),
)
