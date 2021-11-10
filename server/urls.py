from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from health_check import urls as health_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", include(health_urls)),
    path("api/", include("server.apps.movies.api.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
