# Imports
from apps.utilities.models import NamedAPIResource, Effect, FlavorText
from mongoengine import Document, EmbeddedDocument, fields


# Model for ContestTypeRoute
class ContestTypeRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True, unique=True)
    url = fields.StringField(max_length=100, required=True, unique=True)

    # Meta
    meta = {
        "collection": "contest_type_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Embedded Document for ContestName
class ContestName(EmbeddedDocument):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    color = fields.StringField(max_length=100, required=True)
    language = fields.EmbeddedDocumentField(NamedAPIResource)


# Model for ContestType
class ContestType(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    berry_flavor = fields.EmbeddedDocumentField(NamedAPIResource)
    names = fields.ListField(fields.EmbeddedDocumentField(ContestName))

    # Meta
    meta = {
        "collection": "contest_types",
        "indexes": [
            "entity_id",
            "name",
            "berry_flavor",
            "names",
        ],
    }


# Model for ContestEffectRoute
class ContestEffectRoute(Document):
    # Fields
    url = fields.StringField(max_length=100, required=True, unique=True)

    # Meta
    meta = {
        "collection": "contest_effect_routes",
        "indexes": [
            "url",
        ],
    }


# Model for ContestEffect
class ContestEffect(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    appeal = fields.IntField(required=True, min_value=1)
    jam = fields.IntField(required=True, min_value=1)
    effect_entries = fields.ListField(fields.EmbeddedDocumentField(Effect))
    flavor_text_entries = fields.ListField(fields.EmbeddedDocumentField(FlavorText))

    # Meta
    meta = {
        "collection": "contest_effects",
        "indexes": [
            "entity_id",
            "appeal",
            "jam",
            "effect_entries",
            "flavor_text_entries",
        ],
    }


# Model for SuperContestEffectRoute
class SuperContestEffectRoute(Document):
    # Fields
    url = fields.StringField(max_length=100, required=True, unique=True)

    # Meta
    meta = {
        "collection": "super_contest_effect_routes",
        "indexes": [
            "url",
        ],
    }


# Model for SuperContestEffect
class SuperContestEffect(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    appeal = fields.IntField(required=True, min_value=1)
    flavor_text_entries = fields.ListField(fields.EmbeddedDocumentField(FlavorText))
    moves = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))

    # Meta
    meta = {
        "collection": "super_contest_effects",
        "indexes": [
            "entity_id",
            "appeal",
            "flavor_text_entries",
            "moves",
        ],
    }
