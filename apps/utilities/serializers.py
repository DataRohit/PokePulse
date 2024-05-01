# Imports
from rest_framework import serializers


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
