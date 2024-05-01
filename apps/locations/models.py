# Imports
from apps.utilities.models import (
    NamedAPIResource,
    Name,
    GenerationGameIndex,
    VersionEncounterDetail,
)
from mongoengine import Document, EmbeddedDocument, fields


# Model for LocationRoute
class LocationRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "location_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Model for Location
class Location(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True, min_value=1)
    name = fields.StringField(max_length=100, required=True)
    region = fields.EmbeddedDocumentField(NamedAPIResource)
    names = fields.ListField(fields.EmbeddedDocumentField(Name))
    game_indices = fields.ListField(fields.EmbeddedDocumentField(GenerationGameIndex))
    areas = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))

    # Meta
    meta = {
        "collection": "locations",
        "indexes": [
            "entity_id",
            "name",
            "region",
            "names",
            "game_indices",
            "areas",
        ],
    }


# Model for LocationAreaRoute
class LocationAreaRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "location_area_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Embedded Document for PokemonEncounter
class PokemonEncounter(EmbeddedDocument):
    # Fields
    pokemon = fields.EmbeddedDocumentField(NamedAPIResource)
    version_details = fields.ListField(
        fields.EmbeddedDocumentField(VersionEncounterDetail)
    )

    # Meta
    meta = {
        "indexes": ["pokemon", "version_details"],
    }


# Embedded Document for EncounterVersionDetails
class EncounterVersionDetails(EmbeddedDocument):
    # Fields
    rate = fields.IntField(required=True)
    version = fields.EmbeddedDocumentField(NamedAPIResource)

    # Meta
    meta = {
        "indexes": ["rate", "version"],
    }


# Embedded Document for EncounterMethodRate
class EncounterMethodRate(EmbeddedDocument):
    # Fields
    encounter_method = fields.EmbeddedDocumentField(NamedAPIResource)
    version_details = fields.ListField(
        fields.EmbeddedDocumentField(EncounterVersionDetails)
    )

    # Meta
    meta = {
        "indexes": ["encounter_method", "version_details"],
    }


# Model for LocationArea
class LocationArea(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True, min_value=1)
    name = fields.StringField(max_length=100, required=True)
    game_index = fields.IntField(required=True)
    encounter_method_rates = fields.ListField(
        fields.EmbeddedDocumentField(EncounterMethodRate)
    )
    location = fields.EmbeddedDocumentField(NamedAPIResource)
    names = fields.ListField(fields.EmbeddedDocumentField(Name))
    pokemon_encounters = fields.ListField(
        fields.EmbeddedDocumentField(PokemonEncounter)
    )

    # Meta
    meta = {
        "collection": "location_areas",
        "indexes": [
            "entity_id",
            "name",
            "game_index",
            "encounter_method_rates",
            "location",
            "names",
            "pokemon_encounters",
        ],
    }


# Model for PalParkAreaRoute
class PalParkAreaRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "pal_park_area_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Embedded Document for PalParkEncounterSpecies
class PalParkEncounterSpecies(EmbeddedDocument):
    # Fields
    base_score = fields.IntField(required=True)
    rate = fields.IntField(required=True)
    pokemon_species = fields.EmbeddedDocumentField(NamedAPIResource)

    # Meta
    meta = {
        "indexes": ["base_score", "rate", "pokemon_species"],
    }


# Model for PalParkArea
class PalParkArea(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True, min_value=1)
    name = fields.StringField(max_length=100, required=True)
    names = fields.ListField(fields.EmbeddedDocumentField(Name))
    pokemon_encounters = fields.ListField(
        fields.EmbeddedDocumentField(PalParkEncounterSpecies)
    )

    # Meta
    meta = {
        "collection": "pal_park_areas",
        "indexes": [
            "entity_id",
            "name",
            "names",
            "pokemon_encounters",
        ],
    }


# Model for RegionRoute
class RegionRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "region_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Model for Region
class Region(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True, min_value=1)
    locations = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    name = fields.StringField(max_length=100, required=True)
    names = fields.ListField(fields.EmbeddedDocumentField(Name))
    main_generation = fields.EmbeddedDocumentField(NamedAPIResource)
    pokedexes = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    version_groups = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))

    # Meta
    meta = {
        "collection": "regions",
        "indexes": [
            "entity_id",
            "locations",
            "name",
            "names",
            "main_generation",
            "pokedexes",
            "version_groups",
        ],
    }
