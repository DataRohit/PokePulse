# Imports
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


# Set the url patters
urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls, name="django-admin"),
]


# Add API urls
urlpatterns += [
    path("api/", include("apps.core.urls")),
    path("api/", include("apps.base.urls")),
    path("api/", include("apps.berries.urls")),
    path("api/", include("apps.contests.urls")),
    path("api/", include("apps.encounters.urls")),
    path("api/", include("apps.evolutions.urls")),
    path("api/", include("apps.games.urls")),
    path("api/", include("apps.items.urls")),
    path("api/", include("apps.locations.urls")),
    path("api/", include("apps.machines.urls")),
    path("api/", include("apps.moves.urls")),
    path("api/", include("apps.pokemon.urls")),
]


# Swagger settings
schema_view = get_schema_view(
    openapi.Info(
        title="PokePulse API",
        default_version="v1",
        description="**PokePulse: Pokemon Database RestAPI Built using Django Rest Framework**",
        contact=openapi.Contact(email="rohit.vilas.ingole@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# Swagger urls
urlpatterns += [
    path(
        "swagger<format>/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
