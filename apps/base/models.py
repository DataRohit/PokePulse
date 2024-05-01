# Imports
from mongoengine import Document, fields


# Model for BaseRoute
class BaseRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True, unique=True)
    url = fields.StringField(max_length=100, required=True, unique=True)

    # Meta
    meta = {
        "collection": "base_routes",
        "indexes": [
            "name",
            "url",
        ],
    }
