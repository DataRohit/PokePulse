# Imports
from django.urls import path
from apps.games.views import (
    GenerationRouteView,
    GenerationsView,
    PokedexRouteView,
    PokedexesView,
    VersionRouteView,
    VersionsView,
    VersionGroupRouteView,
    VersionGroupsView,
)


# Add the path to router
urlpatterns = [
    path(
        "generation/",
        GenerationRouteView.as_view(),
        name="api--generation-routes",
    ),
    path(
        "generation/<int:entity_id>/",
        GenerationsView.as_view(),
        name="api--generations",
    ),
    path(
        "pokedex/",
        PokedexRouteView.as_view(),
        name="api--pokedex-routes",
    ),
    path(
        "pokedex/<int:entity_id>/",
        PokedexesView.as_view(),
        name="api--pokedexes",
    ),
    path(
        "version/",
        VersionRouteView.as_view(),
        name="api--version-routes",
    ),
    path(
        "version/<int:entity_id>/",
        VersionsView.as_view(),
        name="api--versions",
    ),
    path(
        "version-group/",
        VersionGroupRouteView.as_view(),
        name="api--version-group-routes",
    ),
    path(
        "version-group/<int:entity_id>/",
        VersionGroupsView.as_view(),
        name="api--version-groups",
    ),
]
