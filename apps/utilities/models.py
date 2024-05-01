# Imports
from mongoengine import EmbeddedDocument, fields


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
