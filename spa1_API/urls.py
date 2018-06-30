from django.conf.urls import url
from django.urls import path, include
from django.views.static import serve
from django.conf import settings
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from .routes import build_routes

schema_view = get_schema_view(title='Pastebin API')
router = build_routes()

urlpatterns = [
    path(route='', view=include(router.urls)),

    path(route='schema/', view=schema_view),
    path(route='docs/', view=include_docs_urls(title='Gallery')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
]
