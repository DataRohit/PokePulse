# Imports
from apps.utilities.models import NamedAPIResource
from mongoengine import Document, EmbeddedDocument, fields


# Model for MachineRoute
class MachineRoute(Document):
    # Fields
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "machine_routes",
        "indexes": [
            "url",
        ],
    }


# Model for Machine
class Machine(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    item = fields.EmbeddedDocumentField(NamedAPIResource)
    move = fields.EmbeddedDocumentField(NamedAPIResource)
    version_group = fields.EmbeddedDocumentField(NamedAPIResource)

    # Meta
    meta = {
        "collection": "machines",
        "indexes": [
            "entity_id",
            "item",
            "move",
            "version_group",
        ],
    }
