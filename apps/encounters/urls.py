# Imports
from django.urls import path
from apps.encounters.views import (
    EncounterMethodRouteView,
    EncounterMethodView,
    EncounterConditionRouteView,
    EncounterConditionView,
    EncounterConditionValueRouteView,
    EncounterConditionValueView,
)


# Add the path to router
urlpatterns = [
    path(
        "encounter-method/",
        EncounterMethodRouteView.as_view(),
        name="api--encounter-method-routes",
    ),
    path(
        "encounter-method/<int:entity_id>/",
        EncounterMethodView.as_view(),
        name="api--encounter-methods",
    ),
    path(
        "encounter-condition/",
        EncounterConditionRouteView.as_view(),
        name="api--encounter-condition-routes",
    ),
    path(
        "encounter-condition/<int:entity_id>/",
        EncounterConditionView.as_view(),
        name="api--encounter-conditions",
    ),
    path(
        "encounter-condition-value/",
        EncounterConditionValueRouteView.as_view(),
        name="api--encounter-condition-value-routes",
    ),
    path(
        "encounter-condition-value/<int:entity_id>/",
        EncounterConditionValueView.as_view(),
        name="api--encounter-condition-values",
    ),
]
