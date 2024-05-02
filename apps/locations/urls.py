# Imports
from django.urls import path
from apps.locations.views import (
    LocationRouteView,
    LocationsView,
    LocationAreaRouteView,
    LocationAreasView,
    PalParkAreaRouteView,
    PalParkAreasView,
    RegionRouteView,
    RegionsView,
)


# Add the path to router
urlpatterns = [
    path(
        "location/",
        LocationRouteView.as_view(),
        name="api--location-routes",
    ),
    path(
        "location/<int:entity_id>/",
        LocationsView.as_view(),
        name="api--locations",
    ),
    path(
        "location-area/",
        LocationAreaRouteView.as_view(),
        name="api--location-area-routes",
    ),
    path(
        "location-area/<int:entity_id>/",
        LocationAreasView.as_view(),
        name="api--location-areas",
    ),
    path(
        "pal-park-area/",
        PalParkAreaRouteView.as_view(),
        name="api--pal-park-area-routes",
    ),
    path(
        "pal-park-area/<int:entity_id>/",
        PalParkAreasView.as_view(),
        name="api--pal-park-areas",
    ),
    path(
        "region/",
        RegionRouteView.as_view(),
        name="api--region-routes",
    ),
    path(
        "region/<int:entity_id>/",
        RegionsView.as_view(),
        name="api--regions",
    ),
]
