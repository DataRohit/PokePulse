# Imports
from rest_framework import serializers
from apps.utilities.serializers import NamedAPIResourceSerializer, NameSerializer
from apps.berries.models import (
    BerryRoute,
    Berry,
    BerryFirmnessRoute,
    BerryFirmness,
    BerryFlavorRoute,
    BerryFlavor,
)


# Serializer for BerryRoute
class BerryRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new BaseRoute
    def create(self, validated_data):
        return BerryRoute.objects.create(**validated_data)

    # Method to update a BaseRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for BerryFlavorMap
class BerryFlavorMapSerializer(serializers.Serializer):
    # Fields
    flavor = NamedAPIResourceSerializer()
    potency = serializers.IntegerField(required=True)


# Serializer for Berry
class BerrySerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=100, required=True)
    growth_time = serializers.IntegerField(required=True)
    max_harvest = serializers.IntegerField(required=True)
    natural_gift_power = serializers.IntegerField(required=True)
    size = serializers.IntegerField(required=True)
    smoothness = serializers.IntegerField(required=True)
    soil_dryness = serializers.IntegerField(required=True)
    firmness = NamedAPIResourceSerializer(required=True)
    flavors = BerryFlavorMapSerializer(many=True, required=True)
    item = NamedAPIResourceSerializer(required=True)
    natural_gift_type = NamedAPIResourceSerializer(required=True)

    # Method to create a new Berry
    def create(self, validated_data):
        return Berry.objects.create(**validated_data)

    # Method to update a Berry
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.growth_time = validated_data.get("growth_time", instance.growth_time)
        instance.max_harvest = validated_data.get("max_harvest", instance.max_harvest)
        instance.natural_gift_power = validated_data.get(
            "natural_gift_power", instance.natural_gift_power
        )
        instance.size = validated_data.get("size", instance.size)
        instance.smoothness = validated_data.get("smoothness", instance.smoothness)
        instance.soil_dryness = validated_data.get(
            "soil_dryness", instance.soil_dryness
        )
        instance.firmness = validated_data.get("firmness", instance.firmness)
        instance.flavors = validated_data.get("flavors", instance.flavors)
        instance.item = validated_data.get("item", instance.item)
        instance.natural_gift_type = validated_data.get(
            "natural_gift_type", instance.natural_gift_type
        )
        instance.save()
        return instance


# Serializer for BerryFirmnessRoute
class BerryFirmnessRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new BaseRoute
    def create(self, validated_data):
        return BerryFirmnessRoute.objects.create(**validated_data)

    # Method to update a BaseRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for BerryFirmness
class BerryFirmnessSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=100, required=True)
    berries = NamedAPIResourceSerializer(many=True, required=True)
    names = NameSerializer(many=True, required=True)

    # Method to create a new BerryFirmness
    def create(self, validated_data):
        return BerryFirmness.objects.create(**validated_data)

    # Method to update a BerryFirmness
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.berries = validated_data.get("berries", instance.berries)
        instance.names = validated_data.get("names", instance.names)
        instance.save()
        return instance


# Serializer for BerryFlavorRoute
class BerryFlavorRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new BaseRoute
    def create(self, validated_data):
        return BerryFlavorRoute.objects.create(**validated_data)

    # Method to update a BaseRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for FlavorBerryMap
class FlavorBerryMapSerializer(serializers.Serializer):
    # Fields
    berry = NamedAPIResourceSerializer(required=True)
    potency = serializers.IntegerField(required=True)


# Serializer for BerryFlavor
class BerryFlavorSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=100, required=True)
    berries = FlavorBerryMapSerializer(many=True, required=True)
    contest_type = NamedAPIResourceSerializer(required=True)
    names = NameSerializer(many=True, required=True)

    # Method to create a new BerryFlavor
    def create(self, validated_data):
        return BerryFlavor.objects.create(**validated_data)

    # Method to update a BerryFlavor
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.berries = validated_data.get("berries", instance.berries)
        instance.contest_type = validated_data.get(
            "contest_type", instance.contest_type
        )
        instance.names = validated_data.get("names", instance.names)
        instance.save()
        return instance
