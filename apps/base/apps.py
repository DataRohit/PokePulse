# Imports
from django.apps import AppConfig


# App configurations
class BaseConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.base"
