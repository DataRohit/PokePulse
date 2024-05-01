# Imports
from apps.utilities.models import Name, NamedAPIResource
from mongoengine import Document, fields


# Model for EncounterMethodRoute
class EncounterMethodRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True, unique=True)
    url = fields.StringField(max_length=100, required=True, unique=True)

    # Meta
    meta = {
        "collection": "encounter_method_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Model for EncounterMethod
class EncounterMethod(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True, min_value=1)
    name = fields.StringField(max_length=100, required=True)
    order = fields.IntField(required=True, min_value=1)
    names = fields.ListField(fields.EmbeddedDocumentField(Name))

    # Meta
    meta = {
        "collection": "encounter_methods",
        "indexes": [
            "entity_id",
            "name",
            "order",
            "names",
        ],
    }


# Model for EncounterConditionRoute
class EncounterConditionRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True, unique=True)
    url = fields.StringField(max_length=100, required=True, unique=True)

    # Meta
    meta = {
        "collection": "encounter_condition_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Model for EncounterCondition
class EncounterCondition(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True, min_value=1)
    name = fields.StringField(max_length=100, required=True)
    names = fields.ListField(fields.EmbeddedDocumentField(Name))
    values = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))

    # Meta
    meta = {
        "collection": "encounter_conditions",
        "indexes": [
            "entity_id",
            "name",
            "names",
            "values",
        ],
    }


# Model for EncounterConditionValueRoute
class EncounterConditionValueRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True, unique=True)
    url = fields.StringField(max_length=100, required=True, unique=True)

    # Meta
    meta = {
        "collection": "encounter_condition_value_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Model for EncounterConditionValue
class EncounterConditionValue(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True, min_value=1)
    name = fields.StringField(max_length=100, required=True)
    condition = fields.EmbeddedDocumentField(NamedAPIResource)
    names = fields.ListField(fields.EmbeddedDocumentField(Name))

    # Meta
    meta = {
        "collection": "encounter_condition_values",
        "indexes": ["entity_id", "name", "condition", "names"],
    }
