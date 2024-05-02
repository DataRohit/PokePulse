# Imports
from django.urls import path
from apps.machines.views import (
    MachineRouteView,
    MachinesView,
)


# Add the path to router
urlpatterns = [
    path(
        "machine/",
        MachineRouteView.as_view(),
        name="api--machine-routes",
    ),
    path(
        "machine/<int:entity_id>/",
        MachinesView.as_view(),
        name="api--machines",
    ),
]
