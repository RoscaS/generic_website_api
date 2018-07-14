from . import viewsets

routeList = (
    (r'presentation', viewsets.PresentationViewSet),
    (r'hero', viewsets.HeroViewSet),
    (r'gallery', viewsets.GalleryViewSet),
    (r'contact', viewsets.ContactViewSet),
    (r'review', viewsets.ReviewViewSet),
    (r'promo', viewsets.PromoViewSet),
    (r'options', viewsets.MainOptionsViewSet),
    (r'message', viewsets.MessageViewSet),
)
