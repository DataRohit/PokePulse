# Imports
from django.urls import path
from apps.core.views import CustomObtainAuthToken, CustomCreateUserView, VerifyEmailView


# Add the path to router
urlpatterns = [
    path(
        "obtain-auth-token/",
        CustomObtainAuthToken.as_view(),
        name="api--obtain-auth-token",
    ),
    path(
        "create-user/",
        CustomCreateUserView.as_view(),
        name="api--create-user",
    ),
    path(
        "verify-email/<str:token_key>/",
        VerifyEmailView.as_view(),
        name="api--verify-email",
    ),
]
