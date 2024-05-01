# Imports
from django.urls import path
from apps.contests.views import (
    ContestTypeRouteView,
    ContestTypesView,
    ContestEffectRouteView,
    ContestEffectsView,
    SuperContestEffectRouteView,
    SuperContestEffectsView,
)


# Add the path to router
urlpatterns = [
    path(
        "contest-type/",
        ContestTypeRouteView.as_view(),
        name="api--contest-type-routes",
    ),
    path(
        "contest-type/<int:entity_id>/",
        ContestTypesView.as_view(),
        name="api--contest-types",
    ),
    path(
        "contest-effect/",
        ContestEffectRouteView.as_view(),
        name="api--contest-effect-routes",
    ),
    path(
        "contest-effect/<int:entity_id>/",
        ContestEffectsView.as_view(),
        name="api--contest-effects",
    ),
    path(
        "super-contest-effect/",
        SuperContestEffectRouteView.as_view(),
        name="api--super-contest-effect-routes",
    ),
    path(
        "super-contest-effect/<int:entity_id>/",
        SuperContestEffectsView.as_view(),
        name="api--super-contest-effects",
    ),
]
