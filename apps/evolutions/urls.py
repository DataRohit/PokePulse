# Imports
from django.urls import path
from apps.evolutions.views import (
    EvolutionChainRouteView,
    EvolutionChainView,
    EvolutionTriggerRouteView,
    EvolutionTriggerView,
)


# Add the path to router
urlpatterns = [
    path(
        "evolution-chain/",
        EvolutionChainRouteView.as_view(),
        name="api--evolution-chain-routes",
    ),
    path(
        "evolution-chain/<int:entity_id>/",
        EvolutionChainView.as_view(),
        name="api--evolution-chains",
    ),
    path(
        "evolution-trigger/",
        EvolutionTriggerRouteView.as_view(),
        name="api--evolution-trigger-routes",
    ),
    path(
        "evolution-trigger/<int:entity_id>/",
        EvolutionTriggerView.as_view(),
        name="api--evolution-triggers",
    ),
]
