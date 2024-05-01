# Imports
from rest_framework import serializers
from apps.base.models import BaseRoute


# Serializer for BaseRoute
class BaseRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new BaseRoute
    def create(self, validated_data):
        return BaseRoute.objects.create(**validated_data)

    # Method to update a BaseRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance
