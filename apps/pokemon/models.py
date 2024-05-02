# Imports
from apps.utilities.models import (
    APIResource,
    NamedAPIResource,
    Effect,
    Name,
    VerboseEffect,
    Description,
    VersionGameIndex,
    FlavorText,
    GenerationGameIndex
)
from mongoengine import Document, EmbeddedDocument, fields


# Model for AbilityRoute
class AbilityRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "ability_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Embedded Document for AbilityPokemon
class AbilityPokemon(EmbeddedDocument):
    # Fields
    is_hidden = fields.BooleanField(required=True)
    slot = fields.IntField(required=True)
    pokemon = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded Document for AbilityFlavorText
class AbilityFlavorText(EmbeddedDocument):
    # Fields
    flavor_text = fields.StringField(required=True)
    language = fields.EmbeddedDocumentField(NamedAPIResource)
    version_group = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded Document for AbilityEffectChange
class AbilityEffectChange(EmbeddedDocument):
    # Fields
    effect_entries = fields.ListField(fields.EmbeddedDocumentField(Effect))
    version_group = fields.EmbeddedDocumentField(NamedAPIResource)


# Model for Ability
class Ability(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    is_main_series = fields.BooleanField(required=True)
    generation = fields.EmbeddedDocumentField(NamedAPIResource)
    names = fields.ListField(fields.EmbeddedDocumentField(Name))
    effect_entries = fields.ListField(fields.EmbeddedDocumentField(VerboseEffect))
    effect_changes = fields.ListField(fields.EmbeddedDocumentField(AbilityEffectChange))
    flavor_text_entries = fields.ListField(
        fields.EmbeddedDocumentField(AbilityFlavorText)
    )
    pokemon = fields.ListField(fields.EmbeddedDocumentField(AbilityPokemon))

    # Meta
    meta = {
        "collection": "abilities",
        "indexes": [
            "entity_id",
            "name",
            "is_main_series",
            "generation",
            "names",
            "effect_entries",
            "effect_changes",
            "flavor_text_entries",
            "pokemon",
        ],
    }


# Model for CharacteristicRoute
class CharacteristicRoute(Document):
    # Fields
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "characteristic_routes",
        "indexes": [
            "url",
        ],
    }


# Model for Characteristic
class Characteristic(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    gene_modulo = fields.IntField(required=True)
    possible_values = fields.ListField(fields.IntField(required=True))
    highest_stat = fields.EmbeddedDocumentField(NamedAPIResource)
    descriptions = fields.ListField(fields.EmbeddedDocumentField(Description))

    # Meta
    meta = {
        "collection": "characteristics",
        "indexes": [
            "entity_id",
            "gene_modulo",
            "possible_values",
            "highest_stat",
            "descriptions",
        ],
    }


# Model for EggGroupRoute
class EggGroupRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "egg_group_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Model for EggGroup
class EggGroup(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    names = fields.ListField(fields.EmbeddedDocumentField(Name))
    pokemon_species = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))

    # Meta
    meta = {
        "collection": "egg_groups",
        "indexes": [
            "entity_id",
            "name",
            "names",
            "pokemon_species",
        ],
    }


# Model for GenderRoute
class GenderRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "gender_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Embedded Document for PokemonSpeciesGender
class PokemonSpeciesGender(EmbeddedDocument):
    # Fields
    rate = fields.IntField(required=True)
    pokemon_species = fields.EmbeddedDocumentField(NamedAPIResource)


# Model for Gender
class Gender(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    pokemon_species_details = fields.ListField(
        fields.EmbeddedDocumentField(PokemonSpeciesGender)
    )
    required_for_evolution = fields.ListField(
        fields.EmbeddedDocumentField(NamedAPIResource)
    )

    # Meta
    meta = {
        "collection": "gender",
        "indexes": [
            "entity_id",
            "name",
            "pokemon_species_details",
            "required_for_evolution",
        ],
    }


# Model for GrowthRateRoute
class GrowthRateRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "growth_rate_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Embedded Document for GrowthRateExperienceLevel
class GrowthRateExperienceLevel(EmbeddedDocument):
    # Fields
    level = fields.IntField(required=True)
    experience = fields.IntField(required=True)


# Model for GrowthRate
class GrowthRate(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    formula = fields.StringField(max_length=100, required=True)
    descriptions = fields.ListField(fields.EmbeddedDocumentField(Description))
    levels = fields.ListField(fields.EmbeddedDocumentField(GrowthRateExperienceLevel))
    pokemon_species = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))

    # Meta
    meta = {
        "collection": "growth_rates",
        "indexes": [
            "entity_id",
            "name",
            "formula",
            "descriptions",
            "levels",
            "pokemon_species",
        ],
    }


# Model for NatureRoute
class NatureRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "nature_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Embedded Document for MoveBattleStylePreference
class MoveBattleStylePreference(EmbeddedDocument):
    # Fields
    low_hp_preference = fields.IntField(required=True)
    high_hp_preference = fields.IntField(required=True)
    move_battle_style = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded Document for NatureStatChange
class NatureStatChange(EmbeddedDocument):
    # Fields
    max_change = fields.IntField(required=True)
    pokeathlon_stat = fields.EmbeddedDocumentField(NamedAPIResource)


# Model for Nature
class Nature(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    decreased_stat = fields.EmbeddedDocumentField(NamedAPIResource)
    increased_stat = fields.EmbeddedDocumentField(NamedAPIResource)
    hates_flavor = fields.EmbeddedDocumentField(NamedAPIResource)
    likes_flavor = fields.EmbeddedDocumentField(NamedAPIResource)
    pokeathlon_stat_changes = fields.ListField(
        fields.EmbeddedDocumentField(NatureStatChange)
    )
    move_battle_style_preferences = fields.ListField(
        fields.EmbeddedDocumentField(MoveBattleStylePreference)
    )
    names = fields.ListField(fields.EmbeddedDocumentField(Name))

    # Meta
    meta = {
        "collection": "natures",
        "indexes": [
            "entity_id",
            "name",
            "decreased_stat",
            "increased_stat",
            "hates_flavor",
            "likes_flavor",
            "pokeathlon_stat_changes",
            "move_battle_style_preferences",
            "names",
        ],
    }


# Model for PokeathlonStatRoute
class PokeathlonStatRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "pokeathlon_stat_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Embedded Document for NaturePokeathlonStatAffect
class NaturePokeathlonStatAffect(EmbeddedDocument):
    # Fields
    max_change = fields.IntField(required=True)
    nature = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded Document for NaturePokeathlonStatAffectSets
class NaturePokeathlonStatAffectSets(EmbeddedDocument):
    # Fields
    increase = fields.ListField(
        fields.EmbeddedDocumentField(NaturePokeathlonStatAffect)
    )
    decrease = fields.ListField(
        fields.EmbeddedDocumentField(NaturePokeathlonStatAffect)
    )


# Model for PokeathlonStat
class PokeathlonStat(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    names = fields.ListField(fields.EmbeddedDocumentField(Name))
    affecting_natures = fields.EmbeddedDocumentField(NaturePokeathlonStatAffectSets)

    # Meta
    meta = {
        "collection": "pokeathlon_stats",
        "indexes": [
            "entity_id",
            "name",
            "names",
            "affecting_natures",
        ],
    }


# Model for PokemonRoute
class PokemonRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "pokemon_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Embedded Document for PokemonCries
class PokemonCries(EmbeddedDocument):
    # Fields
    latest = fields.StringField(required=True)
    legacy = fields.StringField(required=True)


# Embedded Document for PokemonSprites
class PokemonSprites(EmbeddedDocument):
    # Fields
    front_default = fields.StringField(required=True)
    front_shiny = fields.StringField(required=True)
    front_female = fields.StringField(required=True)
    front_shiny_female = fields.StringField(required=True)
    back_default = fields.StringField(required=True)
    back_shiny = fields.StringField(required=True)
    back_female = fields.StringField(required=True)
    back_shiny_female = fields.StringField(required=True)
    other = fields.DictField()
    versions = fields.DictField()


# Embedded Document for PokemonStat
class PokemonStat(EmbeddedDocument):
    # Fields
    base_stat = fields.IntField(required=True)
    effort = fields.IntField(required=True)
    stat = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded Document for PokemonMoveVersion
class PokemonMoveVersion(EmbeddedDocument):
    # Fields
    move_learn_method = fields.EmbeddedDocumentField(NamedAPIResource)
    version_group = fields.EmbeddedDocumentField(NamedAPIResource)
    level_learned_at = fields.IntField(required=True)


# Embedded Document for PokemonMove
class PokemonMove(EmbeddedDocument):
    # Fields
    move = fields.EmbeddedDocumentField(NamedAPIResource)
    version_group_details = fields.ListField(
        fields.EmbeddedDocumentField(PokemonMoveVersion)
    )


# Embedded Document for PokemonHeldItemVersion
class PokemonHeldItemVersion(EmbeddedDocument):
    # Fields
    version = fields.EmbeddedDocumentField(NamedAPIResource)
    rarity = fields.IntField(required=True)


# Embedded Document for PokemonHeldItem
class PokemonHeldItem(EmbeddedDocument):
    # Fields
    item = fields.EmbeddedDocumentField(NamedAPIResource)
    version_details = fields.ListField(
        fields.EmbeddedDocumentField(PokemonHeldItemVersion)
    )


# Embedded Document for PokemonType
class PokemonType(EmbeddedDocument):
    # Fields
    slot = fields.IntField(required=True)
    type = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded Document for PokemonFormType
class PokemonFormType(EmbeddedDocument):
    # Fields
    slot = fields.IntField(required=True)
    type = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded Document for PokemonTypePast
class PokemonTypePast(EmbeddedDocument):
    # Fields
    generation = fields.EmbeddedDocumentField(NamedAPIResource)
    types = fields.ListField(fields.EmbeddedDocumentField(PokemonType))


# Embedded Document for PokemonAbility
class PokemonAbility(EmbeddedDocument):
    # Fields
    is_hidden = fields.BooleanField(required=True)
    slot = fields.IntField(required=True)
    ability = fields.EmbeddedDocumentField(NamedAPIResource)


# Model for Pokemon
class Pokemon(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    base_experience = fields.IntField(required=True)
    height = fields.IntField(required=True)
    is_default = fields.BooleanField(required=True)
    order = fields.IntField(required=True)
    weight = fields.IntField(required=True)
    abilities = fields.ListField(fields.EmbeddedDocumentField(PokemonAbility))
    forms = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    game_indices = fields.ListField(fields.EmbeddedDocumentField(VersionGameIndex))
    held_items = fields.ListField(fields.EmbeddedDocumentField(PokemonHeldItem))
    moves = fields.ListField(fields.EmbeddedDocumentField(PokemonMove))
    past_types = fields.ListField(fields.EmbeddedDocumentField(PokemonTypePast))
    sprites = fields.EmbeddedDocumentField(PokemonSprites)
    cries = fields.EmbeddedDocumentField(PokemonCries)
    species = fields.EmbeddedDocumentField(NamedAPIResource)
    stats = fields.ListField(fields.EmbeddedDocumentField(PokemonStat))
    types = fields.ListField(fields.EmbeddedDocumentField(PokemonType))

    # Meta
    meta = {
        "collection": "pokemons",
        "indexes": [
            "entity_id",
            "name",
            "base_experience",
            "height",
            "is_default",
            "order",
            "weight",
            "abilities",
            "forms",
            "game_indices",
            "held_items",
            "moves",
            "past_types",
            "sprites",
            "cries",
            "species",
            "stats",
            "types",
        ],
    }


# Model for PokemonColorRoute
class PokemonColorRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "pokemon_color_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Model for PokemonColor
class PokemonColor(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    names = fields.ListField(fields.EmbeddedDocumentField(Name))
    pokemon_species = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))

    # Meta
    meta = {
        "collection": "pokemon_colors",
        "indexes": [
            "entity_id",
            "name",
            "names",
            "pokemon_species",
        ],
    }


# Model for PokemonFormRoute
class PokemonFormRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "pokemon_form_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Embedded Document for PokemonFormSprites
class PokemonFormSprites(EmbeddedDocument):
    # Fields
    front_default = fields.StringField(required=True)
    front_shiny = fields.StringField(required=True)
    back_default = fields.StringField(required=True)
    back_shiny = fields.StringField(required=True)


# Model for PokemonForm
class PokemonForm(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    order = fields.IntField(required=True)
    form_order = fields.IntField(required=True)
    is_default = fields.BooleanField(required=True)
    is_battle_only = fields.BooleanField(required=True)
    is_mega = fields.BooleanField(required=True)
    form_name = fields.StringField(max_length=100, required=True)
    pokemon = fields.EmbeddedDocumentField(NamedAPIResource)
    types = fields.ListField(fields.EmbeddedDocumentField(PokemonFormType))
    sprites = fields.EmbeddedDocumentField(PokemonFormSprites)
    version_group = fields.EmbeddedDocumentField(NamedAPIResource)
    names = fields.ListField(fields.EmbeddedDocumentField(Name))
    form_names = fields.ListField(fields.EmbeddedDocumentField(Name))

    # Meta
    meta = {
        "collection": "pokemon_forms",
        "indexes": [
            "entity_id",
            "name",
            "order",
            "form_order",
            "is_default",
            "is_battle_only",
            "is_mega",
            "form_name",
            "pokemon",
            "types",
            "sprites",
            "version_group",
            "names",
            "form_names",
        ],
    }


# Model for PokemonHabitatRoute
class PokemonHabitatRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "pokemon_habitat_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Model for PokemonHabitat
class PokemonHabitat(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    names = fields.ListField(fields.EmbeddedDocumentField(Name))
    pokemon_species = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))

    # Meta
    meta = {
        "collection": "pokemon_habitats",
        "indexes": [
            "entity_id",
            "name",
            "names",
            "pokemon_species",
        ],
    }


# Model for PokemonShapeRoute
class PokemonShapeRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "pokemon_shape_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Embedded Document for AwesomeName
class AwesomeName(EmbeddedDocument):
    # Fields
    awesome_name = fields.StringField(required=True)
    language = fields.EmbeddedDocumentField(NamedAPIResource)


# Model for PokemonShape
class PokemonShape(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    awesome_names = fields.ListField(fields.EmbeddedDocumentField(AwesomeName))
    names = fields.ListField(fields.EmbeddedDocumentField(Name))
    pokemon_species = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))

    # Meta
    meta = {
        "collection": "pokemon_shapes",
        "indexes": [
            "entity_id",
            "name",
            "awesome_names",
            "names",
            "pokemon_species",
        ],
    }


# Model for PokemonSpeciesRoute
class PokemonSpeciesRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "pokemon_species_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Embedded Document for PokemonSpeciesVariety
class PokemonSpeciesVariety(EmbeddedDocument):
    # Fields
    is_default = fields.BooleanField(required=True)
    pokemon = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded Document for PalParkEncounterArea
class PalParkEncounterArea(EmbeddedDocument):
    # Fields
    base_score = fields.IntField(required=True)
    rate = fields.IntField(required=True)
    area = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded Document for PokemonSpeciesDexEntry
class PokemonSpeciesDexEntry(EmbeddedDocument):
    # Fields
    entry_number = fields.IntField(required=True)
    pokedex = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded Document for Genus
class Genus(EmbeddedDocument):
    # Fields
    genus = fields.StringField(required=True)
    language = fields.EmbeddedDocumentField(NamedAPIResource)


# Model for PokemonSpecies
class PokemonSpecies(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    order = fields.IntField(required=True)
    gender_rate = fields.IntField(required=True)
    capture_rate = fields.IntField(required=True)
    base_happiness = fields.IntField(required=True)
    is_baby = fields.BooleanField(required=True)
    is_legendary = fields.BooleanField(required=True)
    is_mythical = fields.BooleanField(required=True)
    hatch_counter = fields.IntField(required=True)
    has_gender_differences = fields.BooleanField(required=True)
    forms_switchable = fields.BooleanField(required=True)
    growth_rate = fields.EmbeddedDocumentField(NamedAPIResource)
    pokedex_numbers = fields.ListField(
        fields.EmbeddedDocumentField(PokemonSpeciesDexEntry)
    )
    egg_groups = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    color = fields.EmbeddedDocumentField(NamedAPIResource)
    shape = fields.EmbeddedDocumentField(NamedAPIResource)
    evolves_from_species = fields.EmbeddedDocumentField(NamedAPIResource)
    evolution_chain = fields.EmbeddedDocumentField(APIResource)
    habitat = fields.EmbeddedDocumentField(NamedAPIResource)
    generation = fields.EmbeddedDocumentField(NamedAPIResource)
    names = fields.ListField(fields.EmbeddedDocumentField(Name))
    pal_park_encounters = fields.ListField(
        fields.EmbeddedDocumentField(PalParkEncounterArea)
    )
    flavor_text_entries = fields.ListField(fields.EmbeddedDocumentField(FlavorText))
    form_descriptions = fields.ListField(fields.EmbeddedDocumentField(Description))
    genera = fields.ListField(fields.EmbeddedDocumentField(Genus))
    varieties = fields.ListField(fields.EmbeddedDocumentField(PokemonSpeciesVariety))

    # Meta
    meta = {
        "collection": "pokemon_species",
        "indexes": [
            "entity_id",
            "name",
            "order",
            "gender_rate",
            "capture_rate",
            "base_happiness",
            "is_baby",
            "is_legendary",
            "is_mythical",
            "hatch_counter",
            "has_gender_differences",
            "forms_switchable",
            "growth_rate",
            "pokedex_numbers",
            "egg_groups",
            "color",
            "shape",
            "evolves_from_species",
            "evolution_chain",
            "habitat",
            "generation",
            "names",
            "pal_park_encounters",
            "flavor_text_entries",
            "form_descriptions",
            "genera",
            "varieties",
        ],
    }


# Model for StatRoute
class StatRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "stat_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Embedded Document for NatureStatAffectSets
class NatureStatAffectSets(EmbeddedDocument):
    # Fields
    increase = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    decrease = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))


# Embedded Document for MoveStatAffect
class MoveStatAffect(EmbeddedDocument):
    # Fields
    change = fields.IntField(required=True)
    move = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded Document for MoveStatAffectSets
class MoveStatAffectSets(EmbeddedDocument):
    # Fields
    increase = fields.ListField(fields.EmbeddedDocumentField(MoveStatAffect))
    decrease = fields.ListField(fields.EmbeddedDocumentField(MoveStatAffect))


# Model for Stat
class Stat(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    game_index = fields.IntField(required=True)
    is_battle_only = fields.BooleanField(required=True)
    affecting_moves = fields.EmbeddedDocumentField(MoveStatAffectSets)
    affecting_natures = fields.EmbeddedDocumentField(NatureStatAffectSets)
    characteristics = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    move_damage_class = fields.EmbeddedDocumentField(NamedAPIResource)
    names = fields.ListField(fields.EmbeddedDocumentField(Name))

    # Meta
    meta = {
        "collection": "stats",
        "indexes": [
            "entity_id",
            "name",
            "game_index",
            "is_battle_only",
            "affecting_moves",
            "affecting_natures",
            "characteristics",
            "move_damage_class",
            "names",
        ],
    }


# Model for TypeRoute
class TypeRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "type_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Embedded Document for TypeRelations
class TypeRelations(EmbeddedDocument):
    # Fields
    no_damage_to = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    half_damage_to = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    double_damage_to = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    no_damage_from = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    half_damage_from = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    double_damage_from = fields.ListField(
        fields.EmbeddedDocumentField(NamedAPIResource)
    )


# Embedded Document for TypeRelationsPast
class TypeRelationsPast(EmbeddedDocument):
    # Fields
    generation = fields.EmbeddedDocumentField(NamedAPIResource)
    damage_relations = fields.EmbeddedDocumentField(TypeRelations)


# Embedded Document for TypePokemon
class TypePokemon(EmbeddedDocument):
    # Fields
    slot = fields.IntField(required=True)
    pokemon = fields.EmbeddedDocumentField(NamedAPIResource)


# Model for Type
class Type(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    damage_relations = fields.EmbeddedDocumentField(TypeRelations)
    past_damage_relations = fields.ListField(
        fields.EmbeddedDocumentField(TypeRelationsPast)
    )
    game_indices = fields.ListField(fields.EmbeddedDocumentField(GenerationGameIndex))
    generation = fields.EmbeddedDocumentField(NamedAPIResource)
    move_damage_class = fields.EmbeddedDocumentField(NamedAPIResource)
    names = fields.ListField(fields.EmbeddedDocumentField(Name))
    pokemon = fields.ListField(fields.EmbeddedDocumentField(TypePokemon))
    moves = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))

    # Meta
    meta = {
        "collection": "types",
        "indexes": [
            "entity_id",
            "name",
            "damage_relations",
            "past_damage_relations",
            "game_indices",
            "generation",
            "move_damage_class",
            "names",
            "pokemon",
            "moves",
        ],
    }
