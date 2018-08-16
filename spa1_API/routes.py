from rest_framework import routers
from apps.gallery import urls as gallery_urls
from apps.main import urls as main_urls
from apps.articles import urls as articles_urls


def build_routes():
    routeLists = [
        gallery_urls.routeList,
        main_urls.routeList,
        articles_urls.routeList,
    ]
    router = routers.DefaultRouter()
    for routeList in routeLists:
        for route in routeList:
            router.register(route[0], route[1])

    return router
