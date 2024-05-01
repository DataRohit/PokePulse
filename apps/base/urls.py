# Imports
from django.urls import path
from apps.base.views import BaseRouteView


# Add the path to router
urlpatterns = [
    path(
        "",
        BaseRouteView.as_view(),
        name="api--base-routes",
    ),
]
