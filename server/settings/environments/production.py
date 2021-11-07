"""
This file contains all the settings used in production.
This file is required and if development.py is present these
values are overridden.
"""

from server.settings.components import config

# Production flags:
# https://docs.djangoproject.com/en/3.2/howto/deployment/

DEBUG = False

ALLOWED_HOSTS = [
    # TODO: check production hosts
    config("DOMAIN_NAME"),
    # We need this value for `healthcheck` to work:
    "localhost",
]


# Staticfiles
# https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/

STATIC_ROOT = "/var/www/django/static"

# Media files
# https://docs.djangoproject.com/en/3.2/topics/files/

MEDIA_ROOT = "/var/www/django/media"


# Security
# https://docs.djangoproject.com/en/3.2/topics/security/

SECURE_REDIRECT_EXEMPT = [
    # This is required for healthcheck to work:
    "^health/",
]
