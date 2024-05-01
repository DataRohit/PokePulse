# Imports
from apps.utilities.models import NamedAPIResource, Name
from mongoengine import Document, EmbeddedDocument, fields


# Model for BerryRoute
class BerryRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True, unique=True)
    url = fields.StringField(max_length=100, required=True, unique=True)

    # Meta
    meta = {
        "collection": "berry_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Embedded Document for BerryFlavorMap
class BerryFlavorMap(EmbeddedDocument):
    # Fields
    flavor = fields.EmbeddedDocumentField(NamedAPIResource)
    potency = fields.IntField(required=True)


# Model for Berry
class Berry(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True, min_value=1)
    name = fields.StringField(max_length=100, required=True)
    growth_time = fields.IntField(required=True)
    max_harvest = fields.IntField(required=True)
    natural_gift_power = fields.IntField(required=True)
    size = fields.IntField(required=True)
    smoothness = fields.IntField(required=True)
    soil_dryness = fields.IntField(required=True)
    firmness = fields.EmbeddedDocumentField(NamedAPIResource)
    flavors = fields.ListField(fields.EmbeddedDocumentField(BerryFlavorMap))
    item = fields.EmbeddedDocumentField(NamedAPIResource)
    natural_gift_type = fields.EmbeddedDocumentField(NamedAPIResource)

    # Meta
    meta = {
        "collection": "berries",
        "indexes": [
            "entity_id",
            "name",
            "growth_time",
            "max_harvest",
            "natural_gift_power",
            "size",
            "smoothness",
            "soil_dryness",
            "firmness",
            "flavors",
            "item",
            "natural_gift_type",
        ],
    }


# Model for BerryFirmnessRoute
class BerryFirmnessRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True, unique=True)
    url = fields.StringField(max_length=100, required=True, unique=True)

    # Meta
    meta = {
        "collection": "berry_firmness_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Model for BerryFirmness
class BerryFirmness(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True, min_value=1)
    name = fields.StringField(max_length=100, required=True)
    berries = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    names = fields.ListField(fields.EmbeddedDocumentField(Name))

    # Meta
    meta = {
        "collection": "berry_firmnesses",
        "indexes": ["entity_id", "name", "berries", "names"],
    }


# Model for BerryFlavorRoute
class BerryFlavorRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True, unique=True)
    url = fields.StringField(max_length=100, required=True, unique=True)

    # Meta
    meta = {
        "collection": "berry_flavor_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Embedded Document for FlavorBerryMap
class FlavorBerryMap(EmbeddedDocument):
    # Fields
    berry = fields.EmbeddedDocumentField(NamedAPIResource)
    potency = fields.IntField(required=True)


# Model for BerryFlavor
class BerryFlavor(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True, min_value=1)
    name = fields.StringField(max_length=100, required=True)
    berries = fields.ListField(fields.EmbeddedDocumentField(FlavorBerryMap))
    contest_type = fields.EmbeddedDocumentField(NamedAPIResource)
    names = fields.ListField(fields.EmbeddedDocumentField(Name))

    # Meta
    meta = {
        "collection": "berry_flavors",
        "indexes": ["entity_id", "name", "berries", "contest_type", "names"],
    }
