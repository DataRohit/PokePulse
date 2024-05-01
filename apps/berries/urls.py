# Imports
from django.urls import path
from apps.berries.views import (
    BerryRouteView,
    BerriesView,
    BerryFirmnessRouteView,
    BerryFirmnessesView,
    BerryFlavorRouteView,
    BerryFlavorsView,
)


# Add the path to router
urlpatterns = [
    path(
        "berry/",
        BerryRouteView.as_view(),
        name="api--berry-routes",
    ),
    path(
        "berry/<int:entity_id>/",
        BerriesView.as_view(),
        name="api--berries",
    ),
    path(
        "berry-firmness/",
        BerryFirmnessRouteView.as_view(),
        name="api--berry-firmness-routes",
    ),
    path(
        "berry-firmness/<int:entity_id>/",
        BerryFirmnessesView.as_view(),
        name="api--berry-firmnesses",
    ),
    path(
        "berry-flavor/",
        BerryFlavorRouteView.as_view(),
        name="api--berry-flavor-routes",
    ),
    path(
        "berry-flavor/<int:entity_id>/",
        BerryFlavorsView.as_view(),
        name="api--berry-flavors",
    ),
]
