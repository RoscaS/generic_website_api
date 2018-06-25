from django.urls import path, include
from . import viewsets

from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'images', viewsets.ImageViewSet)
router.register(r'galleries', viewsets.GalleryViewSet)
schema_view = get_schema_view(title='Pastebin api')

urlpatterns = [
    path(route='', view=include(router.urls)),

]
