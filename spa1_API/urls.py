from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework.schemas import get_schema_view

from rest_framework.documentation import include_docs_urls

from django.views.static import serve
from django.conf import settings

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    path(route='', view=include('gallery.urls')),
    # path(route='api-auth/', view=include('rest_framework.urls')),
    path(route='schema/', view=schema_view),
    path(route='docs/', view=include_docs_urls(title='Gallery')),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),


    # path(route='admin/', view=admin.site.urls),

]
