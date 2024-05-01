# Imports
import os
from django.core.wsgi import get_wsgi_application


# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


# Initialize the application
app = get_wsgi_application()
