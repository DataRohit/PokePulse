# Imports
from django.urls import path
from apps.items.views import (
    ItemRouteView,
    ItemsView,
    ItemAttributeRouteView,
    ItemAttributesView,
    ItemCategoryRouteView,
    ItemCategoriesView,
    ItemFlingEffectRouteView,
    ItemFlingEffectsView,
    ItemPocketRouteView,
    ItemPocketsView,
)


# Add the path to router
urlpatterns = [
    path(
        "item/",
        ItemRouteView.as_view(),
        name="api--item-routes",
    ),
    path(
        "item/<int:entity_id>/",
        ItemsView.as_view(),
        name="api--items",
    ),
    path(
        "item-attribute/",
        ItemAttributeRouteView.as_view(),
        name="api--item-attribute-routes",
    ),
    path(
        "item-attribute/<int:entity_id>/",
        ItemAttributesView.as_view(),
        name="api--item-attributes",
    ),
    path(
        "item-category/",
        ItemCategoryRouteView.as_view(),
        name="api--item-category-routes",
    ),
    path(
        "item-category/<int:entity_id>/",
        ItemCategoriesView.as_view(),
        name="api--item-categories",
    ),
    path(
        "item-fling-effect/",
        ItemFlingEffectRouteView.as_view(),
        name="api--item-fling-effect-routes",
    ),
    path(
        "item-fling-effect/<int:entity_id>/",
        ItemFlingEffectsView.as_view(),
        name="api--item-fling-effects",
    ),
    path(
        "item-pocket/",
        ItemPocketRouteView.as_view(),
        name="api--item-pocket-routes",
    ),
    path(
        "item-pocket/<int:entity_id>/",
        ItemPocketsView.as_view(),
        name="api--item-pockets",
    ),
]
