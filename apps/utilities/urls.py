# Imports
from django.urls import path
from apps.utilities.views import LanguageRouteView, LanguagesView


# Add the path to router
urlpatterns = [
    path(
        "language/",
        LanguageRouteView.as_view(),
        name="api--language-routes",
    ),
    path(
        "language/<int:entity_id>/",
        LanguagesView.as_view(),
        name="api--languages",
    ),
]