# Imports
from apps.utilities.models import (
    VerboseEffect,
    MachineVersionDetail,
    Name,
    APIResource,
    NamedAPIResource,
    Description,
)
from apps.pokemon.models import AbilityEffectChange
from mongoengine import Document, EmbeddedDocument, fields


# Model for MoveRoute
class MoveRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "move_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Embedded Document for PastMoveStatValue
class PastMoveStatValue(EmbeddedDocument):
    # Fields
    accuracy = fields.IntField(min_value=0)
    effect_chance = fields.IntField(min_value=0)
    power = fields.IntField(min_value=0)
    pp = fields.IntField(min_value=0)
    effect_entries = fields.ListField(fields.EmbeddedDocumentField(VerboseEffect))
    type = fields.EmbeddedDocumentField(NamedAPIResource)
    version_group = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded Document for MoveStatChange
class MoveStatChange(EmbeddedDocument):
    # Fields
    change = fields.IntField()
    stat = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded Document for MoveMetaData
class MoveMetaData(EmbeddedDocument):
    # Fields
    ailment = fields.EmbeddedDocumentField(NamedAPIResource)
    category = fields.EmbeddedDocumentField(NamedAPIResource)
    min_hits = fields.IntField(min_value=0)
    max_hits = fields.IntField(min_value=0)
    min_turns = fields.IntField(min_value=0)
    max_turns = fields.IntField(min_value=0)
    drain = fields.IntField(min_value=0)
    healing = fields.IntField(min_value=0)
    crit_rate = fields.IntField(min_value=0)
    ailment_chance = fields.IntField(min_value=0)
    flinch_chance = fields.IntField(min_value=0)
    stat_chance = fields.IntField(min_value=0)


# Embedded Document for MoveFlavorText
class MoveFlavorText(EmbeddedDocument):
    # Fields
    flavor_text = fields.StringField(max_length=100, required=True)
    language = fields.EmbeddedDocumentField(NamedAPIResource)
    version_group = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded Document for ContestComboDetail
class ContestComboDetail(EmbeddedDocument):
    # Fields
    use_before = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    use_after = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))


# Embedded Document for ContestComboSets
class ContestComboSets(EmbeddedDocument):
    # Fields
    normal = fields.EmbeddedDocumentField(ContestComboDetail)
    super = fields.EmbeddedDocumentField(ContestComboDetail)


# Model for Move
class Move(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    accuracy = fields.IntField(min_value=0)
    effect_chance = fields.IntField(min_value=0)
    pp = fields.IntField(min_value=0)
    priority = fields.IntField(min_value=0)
    power = fields.IntField(min_value=0)
    contest_combos = fields.EmbeddedDocumentField(ContestComboSets)
    contest_effect = fields.EmbeddedDocumentField(APIResource)
    contest_type = fields.EmbeddedDocumentField(NamedAPIResource)
    damage_class = fields.EmbeddedDocumentField(NamedAPIResource)
    effect_entries = fields.ListField(fields.EmbeddedDocumentField(VerboseEffect))
    effect_changes = fields.ListField(fields.EmbeddedDocumentField(AbilityEffectChange))
    learned_by_pokemon = fields.ListField(
        fields.EmbeddedDocumentField(NamedAPIResource)
    )
    flavor_text_entries = fields.ListField(fields.EmbeddedDocumentField(MoveFlavorText))
    generation = fields.EmbeddedDocumentField(NamedAPIResource)
    machines = fields.ListField(fields.EmbeddedDocumentField(MachineVersionDetail))
    meta_data = fields.EmbeddedDocumentField(MoveMetaData)
    names = fields.ListField(fields.EmbeddedDocumentField(Name))
    past_values = fields.ListField(fields.EmbeddedDocumentField(PastMoveStatValue))
    stat_changes = fields.ListField(fields.EmbeddedDocumentField(MoveStatChange))
    super_contest_effect = fields.EmbeddedDocumentField(APIResource)
    target = fields.EmbeddedDocumentField(NamedAPIResource)
    type = fields.EmbeddedDocumentField(NamedAPIResource)

    # Meta
    meta = {
        "collection": "moves",
        "indexes": [
            "entity_id",
            "name",
            "accuracy",
            "effect_chance",
            "pp",
            "priority",
            "power",
            "contest_combos",
            "contest_type",
            "contest_effect",
            "damage_class",
            "effect_entries",
            "effect_changes",
            "learned_by_pokemon",
            "flavor_text_entries",
            "generation",
            "machines",
            "meta_data",
            "names",
            "past_values",
            "stat_changes",
            "super_contest_effect",
            "target",
            "type",
        ],
    }


# Model for MoveAilmentRoute
class MoveAilmentRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "move_ailment_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Model for MoveAilment
class MoveAilment(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    moves = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    names = fields.ListField(fields.EmbeddedDocumentField(Name))

    # Meta
    meta = {
        "collection": "move_ailments",
        "indexes": [
            "entity_id",
            "name",
            "moves",
            "names",
        ],
    }


# Model for MoveBattleStyleRoute
class MoveBattleStyleRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "move_battle_style_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Model for MoveBattleStyle
class MoveBattleStyle(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    names = fields.ListField(fields.EmbeddedDocumentField(Name))

    # Meta
    meta = {
        "collection": "move_battle_styles",
        "indexes": [
            "entity_id",
            "name",
            "names",
        ],
    }


# Model for MoveCategoryRoute
class MoveCategoryRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "move_category_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Model for MoveCategory
class MoveCategory(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    moves = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    descriptions = fields.ListField(fields.EmbeddedDocumentField(Description))

    # Meta
    meta = {
        "collection": "move_categories",
        "indexes": [
            "entity_id",
            "name",
            "moves",
            "descriptions",
        ],
    }


# Model for MoveDamageClassRoute
class MoveDamageClassRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "move_damage_class_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Model for MoveDamageClass
class MoveDamageClass(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    descriptions = fields.ListField(fields.EmbeddedDocumentField(Description))
    moves = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    names = fields.ListField(fields.EmbeddedDocumentField(Name))

    # Meta
    meta = {
        "collection": "move_damage_classes",
        "indexes": [
            "entity_id",
            "name",
            "descriptions",
            "moves",
            "names",
        ],
    }


# Model for MoveLearnMethodRoute
class MoveLearnMethodRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "move_learn_method_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Model for MoveLearnMethod
class MoveLearnMethod(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    descriptions = fields.ListField(fields.EmbeddedDocumentField(Description))
    names = fields.ListField(fields.EmbeddedDocumentField(Name))
    version_groups = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))

    # Meta
    meta = {
        "collection": "move_learn_methods",
        "indexes": [
            "entity_id",
            "name",
            "descriptions",
            "names",
            "version_groups",
        ],
    }


# Model for MoveTargetRoute
class MoveTargetRoute(Document):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)

    # Meta
    meta = {
        "collection": "move_target_routes",
        "indexes": [
            "name",
            "url",
        ],
    }


# Model for MoveTarget
class MoveTarget(Document):
    # Fields
    entity_id = fields.IntField(required=True, unique=True)
    name = fields.StringField(max_length=100, required=True)
    descriptions = fields.ListField(fields.EmbeddedDocumentField(Description))
    moves = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    names = fields.ListField(fields.EmbeddedDocumentField(Name))

    # Meta
    meta = {
        "collection": "move_targets",
        "indexes": [
            "entity_id",
            "name",
            "descriptions",
            "moves",
            "names",
        ],
    }
