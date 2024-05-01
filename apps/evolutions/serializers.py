# Imports
from rest_framework import serializers
from apps.utilities.serializers import NamedAPIResourceSerializer, NameSerializer
from apps.evolutions.models import (
    EvolutionChainRoute,
    EvolutionChain,
    EvolutionTriggerRoute,
    EvolutionTrigger,
)


# Serializer for EvolutionChainRoute
class EvolutionChainRouteSerializer(serializers.Serializer):
    # Fields
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new EvolutionChainRoute
    def create(self, validated_data):
        return EvolutionChainRoute.objects.create(**validated_data)

    # Method to update a EvolutionChainRoute
    def update(self, instance, validated_data):
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for EvolutionDetail
class EvolutionDetailSerializer(serializers.Serializer):
    # Fields
    item = NamedAPIResourceSerializer(required=False)
    trigger = NamedAPIResourceSerializer(required=False)
    gender = serializers.IntegerField(required=False)
    held_item = NamedAPIResourceSerializer(required=False)
    known_move = NamedAPIResourceSerializer(required=False)
    known_move_type = NamedAPIResourceSerializer(required=False)
    location = NamedAPIResourceSerializer(required=False)
    min_level = serializers.IntegerField(required=False)
    min_happiness = serializers.IntegerField(required=False)
    min_beauty = serializers.IntegerField(required=False)
    min_affection = serializers.IntegerField(required=False)
    needs_overworld_rain = serializers.BooleanField(required=False)
    party_species = NamedAPIResourceSerializer(required=False)
    party_type = NamedAPIResourceSerializer(required=False)
    relative_physical_stats = serializers.IntegerField(required=False)
    time_of_day = serializers.CharField(max_length=100, required=False)
    trade_species = NamedAPIResourceSerializer(required=False)
    turn_upside_down = serializers.BooleanField(required=False)


# Serializer for ChainLink
class ChainLinkSerializer(serializers.Serializer):
    # Fields
    is_baby = serializers.BooleanField(required=False)
    species = NamedAPIResourceSerializer(required=True)
    evolution_details = EvolutionDetailSerializer(many=True, required=False)
    evolves_to = serializers.ListField(child=serializers.DictField(), required=False)


# Serializer for EvolutionChain
class EvolutionChainSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True)
    baby_trigger_item = NamedAPIResourceSerializer(required=False)
    chain = ChainLinkSerializer(required=False)

    # Method to create a new EvolutionChain
    def create(self, validated_data):
        return EvolutionChain.objects.create(**validated_data)

    # Method to update a EvolutionChain
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.baby_trigger_item = validated_data.get(
            "baby_trigger_item", instance.baby_trigger_item
        )
        instance.chain = validated_data.get("chain", instance.chain)
        instance.save()
        return instance


# Serializer for EvolutionTriggerRoute
class EvolutionTriggerRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new EvolutionTriggerRoute
    def create(self, validated_data):
        return EvolutionTriggerRoute.objects.create(**validated_data)

    # Method to update a EvolutionTriggerRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


#  Serializer for EvolutionTrigger
class EvolutionTriggerSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=100, required=True)
    names = NameSerializer(many=True, required=False)
    pokemon_species = NamedAPIResourceSerializer(many=True, required=False)

    # Method to create a new EvolutionTrigger
    def create(self, validated_data):
        return EvolutionTrigger.objects.create(**validated_data)

    # Method to update a EvolutionTrigger
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.names = validated_data.get("names", instance.names)
        instance.pokemon_species = validated_data.get(
            "pokemon_species", instance.pokemon_species
        )
        instance.save()
        return instance
