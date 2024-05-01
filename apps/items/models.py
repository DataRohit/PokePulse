# Imports
from apps.utilities.models import (
    NamedAPIResource,
    VerboseEffect,
    VersionGroupFlavorText,
    GenerationGameIndex,
    Name,
    APIResource,
    MachineVersionDetail,
    Description,
    Effect,
)
from mongoengine import Document, EmbeddedDocument, fields


# Model for ItemRoute
class ItemRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "item_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Embedded Document for ItemHolderPokemonVersionDetail
class ItemHolderPokemonVersionDetail(EmbeddedDocument):
    # Fields
    rarity = fields.IntField(required=True)
    version = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded Document for ItemHolderPokemon
class ItemHolderPokemon(EmbeddedDocument):
    # Fields
    pokemon = fields.EmbeddedDocumentField(NamedAPIResource)
    version_details = fields.ListField(
        fields.EmbeddedDocumentField(ItemHolderPokemonVersionDetail)
    )


# Embedded Document for ItemSprites
class ItemSprites(EmbeddedDocument):
    # Fields
    default = fields.StringField(max_length=100, required=True)


# Model for Item
class Item(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True, min_value=1)
    name = fields.StringField(max_length=100, required=True)
    cost = fields.IntField(required=True)
    fling_power = fields.IntField(required=True)
    fling_effect = fields.EmbeddedDocumentField(NamedAPIResource)
    attributes = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    category = fields.EmbeddedDocumentField(NamedAPIResource)
    effect_entries = fields.ListField(fields.EmbeddedDocumentField(VerboseEffect))
    flavor_text_entries = fields.ListField(
        fields.EmbeddedDocumentField(VersionGroupFlavorText)
    )
    game_indices = fields.ListField(fields.EmbeddedDocumentField(GenerationGameIndex))
    names = fields.ListField(fields.EmbeddedDocumentField(Name))
    sprites = fields.EmbeddedDocumentField(ItemSprites)
    held_by_pokemon = fields.ListField(fields.EmbeddedDocumentField(ItemHolderPokemon))
    baby_trigger_for = fields.EmbeddedDocumentField(APIResource)
    machines = fields.ListField(fields.EmbeddedDocumentField(MachineVersionDetail))

    # Meta
    meta = {
        "collection": "items",
        "indexes": [
            "entity_id",
            "name",
            "cost",
            "fling_power",
            "fling_effect",
            "attributes",
            "category",
            "effect_entries",
            "flavor_text_entries",
            "game_indices",
            "names",
            "held_by_pokemon",
            "baby_trigger_for",
            "machines",
            "sprites",
        ],
    }


# Model for ItemAttributeRoute
class ItemAttributeRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "item_attribute_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Model for ItemAttribute
class ItemAttribute(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True, min_value=1)
    name = fields.StringField(max_length=100, required=True)
    items = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    names = fields.ListField(fields.EmbeddedDocumentField(Name))
    descriptions = fields.ListField(fields.EmbeddedDocumentField(Description))

    # Meta
    meta = {
        "collection": "item_attributes",
        "indexes": [
            "entity_id",
            "name",
            "items",
            "names",
            "descriptions",
        ],
    }


# Model for ItemCategoryRoute
class ItemCategoryRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "item_category_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Model for ItemCategory
class ItemCategory(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True, min_value=1)
    name = fields.StringField(max_length=100, required=True)
    items = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    names = fields.ListField(fields.EmbeddedDocumentField(Name))
    pocket = fields.EmbeddedDocumentField(NamedAPIResource)

    # Meta
    meta = {
        "collection": "item_categories",
        "indexes": [
            "entity_id",
            "name",
            "items",
            "names",
            "pocket",
        ],
    }


# Model for ItemFlingEffectRoute
class ItemFlingEffectRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "item_fling_effect_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Model for ItemFlingEffect
class ItemFlingEffect(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True, min_value=1)
    name = fields.StringField(max_length=100, required=True)
    effect_entries = fields.ListField(fields.EmbeddedDocumentField(Effect))
    items = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))

    # Meta
    meta = {
        "collection": "item_fling_effects",
        "indexes": [
            "entity_id",
            "name",
            "effect_entries",
            "items",
        ],
    }


# Model for ItemPocketRoute
class ItemPocketRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "item_pocket_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Model for ItemPocket
class ItemPocket(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True, min_value=1)
    name = fields.StringField(max_length=100, required=True)
    categories = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    names = fields.ListField(fields.EmbeddedDocumentField(Name))

    # Meta
    meta = {
        "collection": "item_pockets",
        "indexes": [
            "entity_id",
            "name",
            "categories",
            "names",
        ],
    }
