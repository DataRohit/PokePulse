# Imports
from rest_framework import serializers
from apps.utilities.serializers import NamedAPIResourceSerializer
from apps.machines.models import MachineRoute, Machine


# Serializer for MachineRoute
class MachineRouteSerializer(serializers.Serializer):
    # Fields
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new MachineRoute
    def create(self, validated_data):
        return MachineRoute.objects.create(**validated_data)

    # Method to update a MachineRoute
    def update(self, instance, validated_data):
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for Machine
class MachineSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True, min_value=1)
    item = NamedAPIResourceSerializer()
    move = NamedAPIResourceSerializer()
    version_group = NamedAPIResourceSerializer()

    # Method to create a new Machine
    def create(self, validated_data):
        return Machine.objects.create(**validated_data)

    # Method to update a Machine
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.item = validated_data.get("item", instance.item)
        instance.move = validated_data.get("move", instance.move)
        instance.version_group = validated_data.get(
            "version_group", instance.version_group
        )
        instance.save()
        return instance
