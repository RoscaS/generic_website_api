from . import viewsets

routeList = (
    (r'texts', viewsets.TextsViewSet),

    (r'presentation', viewsets.PresentationViewSet),
    (r'hero', viewsets.HeroViewSet),
    (r'events', viewsets.EventsViewSet),
    (r'contact', viewsets.ContactViewSet),
    (r'review', viewsets.ReviewViewSet),
    (r'promo', viewsets.PromoViewSet),
    (r'options', viewsets.MainOptionsViewSet),
    (r'message', viewsets.MessageViewSet),
)
