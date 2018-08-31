from django.conf.urls import url
from django.urls import path, include
from django.views.static import serve
from django.conf import settings
from django.views.generic.base import RedirectView
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from rest_framework_jwt.views import obtain_jwt_token

from .routes import build_routes



schema_view = get_schema_view(title='Pastebin API')
router = build_routes()

urlpatterns = [
    path(route='', view=RedirectView.as_view(url='api/', permanent=False)),
    path(route='api/', view=include(router.urls)),

    path(route='api-auth', view=include('rest_framework.urls')),
    path(route='auth/token/', view=obtain_jwt_token),

    path(route='schema/', view=schema_view),
    path(route='docs/', view=include_docs_urls(title='Gallery')),


    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
]
