# Imports
from rest_framework import serializers
from apps.utilities.serializers import (
    NamedAPIResourceSerializer,
    EffectSerializer,
    FlavorTextSerializer,
)
from apps.contests.models import (
    ContestTypeRoute,
    ContestType,
    ContestEffectRoute,
    ContestEffect,
    SuperContestEffectRoute,
    SuperContestEffect,
)


# Serializer for ContestTypeRoute
class ContestTypeRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new ContestTypeRoute
    def create(self, validated_data):
        return ContestTypeRoute.objects.create(**validated_data)

    # Method to update a ContestTypeRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for ContestName
class ContestNameSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    color = serializers.CharField(max_length=100, required=True)
    language = NamedAPIResourceSerializer()


# Serializer for ContestType
class ContestTypeSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=100, required=True)
    berry_flavor = NamedAPIResourceSerializer(required=True)
    names = ContestNameSerializer(many=True, required=True)

    # Method to create a new ContestType
    def create(self, validated_data):
        return ContestType.objects.create(**validated_data)

    # Method to update a ContestType
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.berry_flavor = validated_data.get(
            "berry_flavor", instance.berry_flavor
        )
        instance.names = validated_data.get("names", instance.names)
        instance.save()
        return instance


# Serializer for ContestEffectRoute
class ContestEffectRouteSerializer(serializers.Serializer):
    # Fields
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new ContestEffectRoute
    def create(self, validated_data):
        return ContestEffectRoute.objects.create(**validated_data)

    # Method to update a ContestEffectRoute
    def update(self, instance, validated_data):
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for ContestEffect
class ContestEffectSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True)
    appeal = serializers.IntegerField(required=True)
    jam = serializers.IntegerField(required=True)
    effect_entries = EffectSerializer(many=True, required=True)
    flavor_text_entries = FlavorTextSerializer(many=True, required=True)

    # Method to create a new ContestEffect
    def create(self, validated_data):
        return ContestEffect.objects.create(**validated_data)

    # Method to update a ContestEffect
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.appeal = validated_data.get("appeal", instance.appeal)
        instance.jam = validated_data.get("jam", instance.jam)
        instance.effect_entries = validated_data.get(
            "effect_entries", instance.effect_entries
        )
        instance.flavor_text_entries = validated_data.get(
            "flavor_text_entries", instance.flavor_text_entries
        )
        instance.save()
        return instance


# Serializer for SuperContestEffectRoute
class SuperContestEffectRouteSerializer(serializers.Serializer):
    # Fields
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new SuperContestEffectRoute
    def create(self, validated_data):
        return SuperContestEffectRoute.objects.create(**validated_data)

    # Method to update a SuperContestEffectRoute
    def update(self, instance, validated_data):
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for SuperContestEffect
class SuperContestEffectSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True)
    appeal = serializers.IntegerField(required=True)
    flavor_text_entries = FlavorTextSerializer(many=True, required=True)
    moves = NamedAPIResourceSerializer(many=True, required=True)

    # Method to create a new SuperContestEffect
    def create(self, validated_data):
        return SuperContestEffect.objects.create(**validated_data)

    # Method to update a SuperContestEffect
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.appeal = validated_data.get("appeal", instance.appeal)
        instance.flavor_text_entries = validated_data.get(
            "flavor_text_entries", instance.flavor_text_entries
        )
        instance.moves = validated_data.get("moves", instance.moves)
        instance.save()
        return instance
