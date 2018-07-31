from django.apps import AppConfig


class GalleryConfig(AppConfig):
    name = 'apps.gallery'

    def ready(self):
        import apps.gallery.signals
