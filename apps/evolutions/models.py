# Imports
from apps.utilities.models import NamedAPIResource, Name
from mongoengine import Document, EmbeddedDocument, fields


# Model for EvolutionChainRoute
class EvolutionChainRoute(Document):
    # Fields
    url = fields.StringField(max_length=100, required=True, unique=True)

    # Meta
    meta = {
        "collection": "evolution_chain_routes",
        "indexes": [
            "url",
        ],
    }


# Embedded Document for EvolutionDetail
class EvolutionDetail(EmbeddedDocument):
    # Fields
    item = fields.EmbeddedDocumentField(NamedAPIResource)
    trigger = fields.EmbeddedDocumentField(NamedAPIResource)
    gender = fields.IntField(required=False)
    held_item = fields.EmbeddedDocumentField(NamedAPIResource)
    known_move = fields.EmbeddedDocumentField(NamedAPIResource)
    known_move_type = fields.EmbeddedDocumentField(NamedAPIResource)
    location = fields.EmbeddedDocumentField(NamedAPIResource)
    min_level = fields.IntField(required=True)
    min_happiness = fields.IntField(required=False)
    min_beauty = fields.IntField(required=False)
    min_affection = fields.IntField(required=False)
    needs_overworld_rain = fields.BooleanField(required=False)
    party_species = fields.EmbeddedDocumentField(NamedAPIResource)
    party_type = fields.EmbeddedDocumentField(NamedAPIResource)
    relative_physical_stats = fields.IntField(required=False)
    time_of_day = fields.StringField(max_length=100, required=False)
    trade_species = fields.EmbeddedDocumentField(NamedAPIResource)
    turn_upside_down = fields.BooleanField(required=True)


# Embedded Document for ChainLink
class ChainLink(EmbeddedDocument):
    # Fields
    is_baby = fields.BooleanField(required=True)
    species = fields.EmbeddedDocumentField(NamedAPIResource)
    evolution_details = fields.ListField(fields.EmbeddedDocumentField(EvolutionDetail))
    evolves_to = fields.ListField()


# Model for EvolutionChain
class EvolutionChain(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    baby_trigger_item = fields.EmbeddedDocumentField(NamedAPIResource)
    chain = fields.EmbeddedDocumentField(ChainLink)

    # Meta
    meta = {
        "collection": "evolution_chains",
        "indexes": [
            "entity_id",
            "chain",
        ],
    }


# Model for EvolutionTriggerRoute
class EvolutionTriggerRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True, unique=True)
    url = fields.StringField(max_length=100, required=True, unique=True)

    # Meta
    meta = {
        "collection": "evolution_trigger_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Model for EvolutionTrigger
class EvolutionTrigger(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    names = fields.ListField(fields.EmbeddedDocumentField(Name))
    pokemon_species = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))

    # Meta
    meta = {
        "collection": "evolution_triggers",
        "indexes": [
            "entity_id",
            "name",
            "names",
            "pokemon_species",
        ],
    }
