# Imports
from apps.utilities.models import NamedAPIResource, Name, Description
from mongoengine import Document, EmbeddedDocument, fields


# Model for GenerationRoute
class GenerationRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True, unique=True)
    url = fields.StringField(max_length=100, required=True, unique=True)

    # Meta
    meta = {
        "collection": "generation_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Model for Generation
class Generation(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    abilities = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    names = fields.ListField(fields.EmbeddedDocumentField(Name))
    main_region = fields.EmbeddedDocumentField(NamedAPIResource)
    moves = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    pokemon_species = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    types = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    version_groups = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))

    # Meta
    meta = {
        "collection": "generations",
        "indexes": [
            "entity_id",
            "name",
            "abilities",
            "names",
            "main_region",
            "moves",
            "pokemon_species",
            "types",
            "version_groups",
        ],
    }


# Model for PokedexRoute
class PokedexRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True, unique=True)
    url = fields.StringField(max_length=100, required=True, unique=True)

    # Meta
    meta = {
        "collection": "pokedex_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Embedded Document for PokemonEntry
class PokemonEntry(EmbeddedDocument):
    # Fields
    entry_number = fields.IntField(required=True)
    pokemon_species = fields.EmbeddedDocumentField(NamedAPIResource)

    # Meta
    meta = {
        "indexes": [
            "entry_number",
            "pokemon_species",
        ],
    }


# Model for Pokedex
class Pokedex(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    is_main_series = fields.BooleanField(required=True)
    descriptions = fields.ListField(fields.EmbeddedDocumentField(Description))
    names = fields.ListField(fields.EmbeddedDocumentField(Name))
    pokemon_entries = fields.ListField(fields.EmbeddedDocumentField(PokemonEntry))
    region = fields.EmbeddedDocumentField(NamedAPIResource)
    version_groups = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))

    # Meta
    meta = {
        "collection": "pokedexes",
        "indexes": [
            "entity_id",
            "name",
            "is_main_series",
            "descriptions",
            "names",
            "pokemon_entries",
            "region",
            "version_groups",
        ],
    }


# Model for VersionRoute
class VersionRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True, unique=True)
    url = fields.StringField(max_length=100, required=True, unique=True)

    # Meta
    meta = {
        "collection": "version_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Model for Version
class Version(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    names = fields.ListField(fields.EmbeddedDocumentField(Name))
    version_group = fields.EmbeddedDocumentField(NamedAPIResource)

    # Meta
    meta = {
        "collection": "versions",
        "indexes": [
            "entity_id",
            "name",
            "names",
            "version_group",
        ],
    }


# Model for VersionGroupRoute
class VersionGroupRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True, unique=True)
    url = fields.StringField(max_length=100, required=True, unique=True)

    # Meta
    meta = {
        "collection": "version_group_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Model for VersionGroup
class VersionGroup(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    order = fields.IntField(required=True)
    generation = fields.EmbeddedDocumentField(NamedAPIResource)
    move_learn_methods = fields.ListField(
        fields.EmbeddedDocumentField(NamedAPIResource)
    )
    pokedexes = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    regions = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    versions = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))

    # Meta
    meta = {
        "collection": "version_groups",
        "indexes": [
            "entity_id",
            "name",
            "order",
            "generation",
            "move_learn_methods",
            "pokedexes",
            "regions",
            "versions",
        ],
    }
