# Imports
from rest_framework import serializers
from apps.utilities.serializers import NameSerializer, NamedAPIResourceSerializer
from apps.encounters.models import (
    EncounterMethodRoute,
    EncounterMethod,
    EncounterConditionRoute,
    EncounterCondition,
    EncounterConditionValueRoute,
    EncounterConditionValue,
)


# Serializer for EncounterMethodRoute
class EncounterMethodRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new EncounterMethodRoute
    def create(self, validated_data):
        return EncounterMethodRoute.objects.create(**validated_data)

    # Method to update an EncounterMethodRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for EncounterMethod
class EncounterMethodSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=100, required=True)
    order = serializers.IntegerField(required=True)
    names = NameSerializer(many=True, required=True)

    # Method to create a new EncounterMethod
    def create(self, validated_data):
        return EncounterMethod.objects.create(**validated_data)

    # Method to update an EncounterMethod
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.order = validated_data.get("order", instance.order)
        instance.names = validated_data.get("names", instance.names)
        instance.save()
        return instance


# Serializer for EncounterConditionRoute
class EncounterConditionRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new EncounterConditionRoute
    def create(self, validated_data):
        return EncounterConditionRoute.objects.create(**validated_data)

    # Method to update an EncounterConditionRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for EncounterCondition
class EncounterConditionSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=100, required=True)
    names = NameSerializer(many=True, required=True)
    values = NamedAPIResourceSerializer(many=True, required=True)

    # Method to create a new EncounterCondition
    def create(self, validated_data):
        return EncounterCondition.objects.create(**validated_data)

    # Method to update an EncounterCondition
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.names = validated_data.get("names", instance.names)
        instance.values = validated_data.get("values", instance.values)
        instance.save()


# Serializer for EncounterConditionValueRoute
class EncounterConditionValueRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new EncounterConditionValueRoute
    def create(self, validated_data):
        return EncounterConditionValueRoute.objects.create(**validated_data)

    # Method to update an EncounterConditionValueRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for EncounterConditionValue
class EncounterConditionValueSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=100, required=True)
    condition = NamedAPIResourceSerializer(required=True)
    names = NameSerializer(many=True, required=True)

    # Method to create a new EncounterConditionValue
    def create(self, validated_data):
        return EncounterConditionValue.objects.create(**validated_data)

    # Method to update an EncounterConditionValue
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.condition = validated_data.get("condition", instance.condition)
        instance.names = validated_data.get("names", instance.names)
        instance.save()
