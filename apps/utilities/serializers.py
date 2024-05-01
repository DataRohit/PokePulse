# Imports
from rest_framework import serializers


# Serializer for APIResource
class APIResourceSerializer(serializers.Serializer):
    # Fields
    url = serializers.CharField(max_length=100, required=True)


# Serializer for NamedAPIResource
class NamedAPIResourceSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)


# Serializer for Description
class DescriptionSerializer(serializers.Serializer):
    # Fields
    description = serializers.CharField(max_length=255, required=True)
    language = NamedAPIResourceSerializer()


# Serializer for Name
class NameSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    language = NamedAPIResourceSerializer()


# Serializer for Effect
class EffectSerializer(serializers.Serializer):
    # Fields
    effect = serializers.CharField(max_length=100, required=True)
    language = NamedAPIResourceSerializer()


# Serializer for FlavorText
class FlavorTextSerializer(serializers.Serializer):
    # Fields
    flavor_text = serializers.CharField(max_length=100, required=True)
    language = NamedAPIResourceSerializer()
    version = NamedAPIResourceSerializer()


# Serializer for Encounter
class EncounterSerializer(serializers.Serializer):
    # Fields
    min_level = serializers.IntegerField(required=True)
    max_level = serializers.IntegerField(required=True)
    condition_values = NamedAPIResourceSerializer(many=True)
    chance = serializers.IntegerField(required=True)
    method = NamedAPIResourceSerializer()


# Serializer for FlavorText
class FlavorTextSerializer(serializers.Serializer):
    # Fields
    flavor_text = serializers.CharField(required=True)
    language = NamedAPIResourceSerializer()
    version = NamedAPIResourceSerializer()


# Serializer for GenerationGameIndex
class GenerationGameIndexSerializer(serializers.Serializer):
    # Fields
    game_index = serializers.IntegerField(required=True)
    generation = NamedAPIResourceSerializer()


# Serializer for MachineVersionDetail
class MachineVersionDetailSerializer(serializers.Serializer):
    # Fields
    machine = NamedAPIResourceSerializer()
    version_group = NamedAPIResourceSerializer()


# Serializer for VerboseEffect
class VerboseEffectSerializer(serializers.Serializer):
    # Fields
    effect = serializers.CharField(required=True)
    short_effect = serializers.CharField(required=True)
    language = NamedAPIResourceSerializer()


# Serializer for VersionEncounterDetail
class VersionEncounterDetailSerializer(serializers.Serializer):
    # Fields
    version = NamedAPIResourceSerializer()
    max_chance = serializers.IntegerField(required=True)
    encounter_details = EncounterSerializer(many=True)


# Serializer for VersionGameIndex
class VersionGameIndexSerializer(serializers.Serializer):
    # Fields
    game_index = serializers.IntegerField(required=True)
    version = NamedAPIResourceSerializer()


# Serializer for VersionGroupFlavorText
class VersionGroupFlavorTextSerializer(serializers.Serializer):
    # Fields
    text = serializers.CharField(required=True)
    language = NamedAPIResourceSerializer()
    version_group = NamedAPIResourceSerializer()
