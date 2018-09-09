"""
WSGI config for spa1_API project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ['HTTPS'] = "on"
os.environ['wsgi.url_scheme'] = "https"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spa1_API.settings")

application = get_wsgi_application()
