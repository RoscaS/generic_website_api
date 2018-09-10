from . import viewsets

routeList = (
    (r'authtest', viewsets.AuthTestViewSet),
    (r'presentation', viewsets.PresentationViewSet),
    (r'hero', viewsets.HeroViewSet),
    (r'article', viewsets.ArticlesViewSet),
    (r'events', viewsets.EventsViewSet),
    (r'contact', viewsets.ContactViewSet),
    (r'promo', viewsets.PromoViewSet),
    (r'message', viewsets.MessageViewSet),
    (r'siteInfo', viewsets.SiteInformationsViewSet),
    (r'siteContact', viewsets.SiteContactViewSet),
    (r'siteOptions', viewsets.SiteOptionsViewSet),
)
