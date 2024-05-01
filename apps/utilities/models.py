# Imports
from mongoengine import EmbeddedDocument, fields


# Embedded Document for APIResource
class APIResource(EmbeddedDocument):
    # Fields
    url = fields.StringField(max_length=100, required=True)


# Embedded Document for NamedAPIResource
class NamedAPIResource(EmbeddedDocument):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    url = fields.StringField(max_length=100, required=True)


# Embedded Document for Description
class Description(EmbeddedDocument):
    # Fields
    description = fields.StringField(max_length=255, required=True)
    language = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded Document for Name
class Name(EmbeddedDocument):
    # Fields
    name = fields.StringField(max_length=100, required=True)
    language = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded Document for Effect
class Effect(EmbeddedDocument):
    # Fields
    effect = fields.StringField(max_length=100, required=True)
    language = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded Document for FlavorText
class FlavorText(EmbeddedDocument):
    # Fields
    flavor_text = fields.StringField(max_length=100, required=True)
    language = fields.EmbeddedDocumentField(NamedAPIResource)
    version = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded Document for Encounter
class Encounter(EmbeddedDocument):
    # Fields
    min_level = fields.IntField(required=True)
    max_level = fields.IntField(required=True)
    condition_values = fields.ListField(fields.EmbeddedDocumentField(NamedAPIResource))
    chance = fields.IntField(required=True)
    method = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded Document for FlavorText
class FlavorText(EmbeddedDocument):
    # Fields
    flavor_text = fields.StringField(required=True)
    language = fields.EmbeddedDocumentField(NamedAPIResource)
    version = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded Document for GenerationGameIndex
class GenerationGameIndex(EmbeddedDocument):
    # Fields
    game_index = fields.IntField(required=True)
    generation = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded Document for MachineVersionDetail
class MachineVersionDetail(EmbeddedDocument):
    # Fields
    machine = fields.EmbeddedDocumentField(APIResource)
    version_group = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded Document for VerboseEffect
class VerboseEffect(EmbeddedDocument):
    # Fields
    effect = fields.StringField(max_length=100, required=True)
    short_effect = fields.StringField(max_length=100, required=True)
    language = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded Document for VersionEncounterDetail
class VersionEncounterDetail(EmbeddedDocument):
    # Fields
    version = fields.EmbeddedDocumentField(NamedAPIResource)
    max_chance = fields.IntField(required=True)
    encounter_details = fields.ListField(fields.EmbeddedDocumentField(Encounter))


# Embedded Document for VersionGameIndex
class VersionGameIndex(EmbeddedDocument):
    # Fields
    game_index = fields.IntField(required=True)
    version = fields.EmbeddedDocumentField(NamedAPIResource)


# Embedded VersionGroupFlavorText
class VersionGroupFlavorText(EmbeddedDocument):
    # Fields
    text = fields.StringField(max_length=100, required=True)
    language = fields.EmbeddedDocumentField(NamedAPIResource)
    version_group = fields.EmbeddedDocumentField(NamedAPIResource)
