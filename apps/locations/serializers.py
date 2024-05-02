# Imports
from rest_framework import serializers
from apps.utilities.serializers import (
    NamedAPIResourceSerializer,
    NameSerializer,
    GenerationGameIndexSerializer,
    VersionEncounterDetailSerializer,
)
from apps.locations.models import (
    LocationRoute,
    Location,
    LocationAreaRoute,
    LocationArea,
    PalParkAreaRoute,
    PalParkArea,
    RegionRoute,
    Region,
)


# Serializer for LocationRoute
class LocationRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new LocationRoute
    def create(self, validated_data):
        return LocationRoute.objects.create(**validated_data)

    # Method to update a LocationRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for Location
class LocationSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True, min_value=1)
    name = serializers.CharField(max_length=100, required=True)
    region = NamedAPIResourceSerializer()
    names = NameSerializer(many=True)
    game_indices = GenerationGameIndexSerializer(many=True)
    areas = NamedAPIResourceSerializer(many=True)

    # Method to create a new Location
    def create(self, validated_data):
        return Location.objects.create(**validated_data)

    # Method to update a Location
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.region = validated_data.get("region", instance.region)
        instance.names = validated_data.get("names", instance.names)
        instance.game_indices = validated_data.get(
            "game_indices", instance.game_indices
        )
        instance.areas = validated_data.get("areas", instance.areas)
        instance.save()
        return instance


# Serializer for LocationAreaRoute
class LocationAreaRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new LocationAreaRoute
    def create(self, validated_data):
        return LocationAreaRoute.objects.create(**validated_data)

    # Method to update a LocationAreaRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for PokemonEncounter
class PokemonEncounterSerializer(serializers.Serializer):
    # Fields
    pokemon = NamedAPIResourceSerializer()
    version_details = VersionEncounterDetailSerializer(many=True)


# Serializer for EncounterVersionDetail
class EncounterVersionDetailSerializer(serializers.Serializer):
    # Fields
    rate = serializers.IntegerField(required=True)
    version = NamedAPIResourceSerializer()


# Serializer for EncounterMethodRate
class EncounterMethodRateSerializer(serializers.Serializer):
    # Fields
    encounter_method = NamedAPIResourceSerializer()
    version_details = EncounterVersionDetailSerializer(many=True)


# Serializer for LocationArea
class LocationAreaSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True, min_value=1)
    name = serializers.CharField(max_length=100, required=True)
    game_index = serializers.IntegerField(required=True)
    encounter_method_rates = EncounterMethodRateSerializer(many=True)
    location = NamedAPIResourceSerializer()
    names = NameSerializer(many=True)
    pokemon_encounters = PokemonEncounterSerializer(many=True)

    # Method to create a new LocationArea
    def create(self, validated_data):
        return LocationArea.objects.create(**validated_data)

    # Method to update a LocationArea
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.game_index = validated_data.get("game_index", instance.game_index)
        instance.encounter_method_rates = validated_data.get(
            "encounter_method_rates", instance.encounter_method_rates
        )
        instance.location = validated_data.get("location", instance.location)
        instance.names = validated_data.get("names", instance.names)
        instance.pokemon_encounters = validated_data.get(
            "pokemon_encounters", instance.pokemon_encounters
        )
        instance.save()
        return instance


# Serializer for PalParkAreaRoute
class PalParkAreaRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new PalParkAreaRoute
    def create(self, validated_data):
        return PalParkAreaRoute.objects.create(**validated_data)

    # Method to update a PalParkAreaRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for PalParkEncounterSpecies
class PalParkEncounterSpeciesSerializer(serializers.Serializer):
    # Fields
    base_score = serializers.IntegerField(required=True)
    rate = serializers.IntegerField(required=True)
    pokemon_species = NamedAPIResourceSerializer()


# Serializer for PalParkArea
class PalParkAreaSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True, min_value=1)
    name = serializers.CharField(max_length=100, required=True)
    names = NameSerializer(many=True)
    pokemon_encounters = PalParkEncounterSpeciesSerializer(many=True)

    # Method to create a new PalParkArea
    def create(self, validated_data):
        return PalParkArea.objects.create(**validated_data)

    # Method to update a PalParkArea
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.names = validated_data.get("names", instance.names)
        instance.pokemon_encounters = validated_data.get(
            "pokemon_encounters", instance.pokemon_encounters
        )
        instance.save()
        return instance


# Serializer for RegionRoute
class RegionRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new RegionRoute
    def create(self, validated_data):
        return RegionRoute.objects.create(**validated_data)

    # Method to update a RegionRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for Region
class RegionSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True, min_value=1)
    locations = NamedAPIResourceSerializer(many=True)
    name = serializers.CharField(max_length=100, required=True)
    names = NameSerializer(many=True)
    main_generation = NamedAPIResourceSerializer()
    pokedexes = NamedAPIResourceSerializer(many=True)
    version_groups = NamedAPIResourceSerializer(many=True)

    # Method to create a new Region
    def create(self, validated_data):
        return Region.objects.create(**validated_data)

    # Method to update a Region
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.locations = validated_data.get("locations", instance.locations)
        instance.name = validated_data.get("name", instance.name)
        instance.names = validated_data.get("names", instance.names)
        instance.main_generation = validated_data.get(
            "main_generation", instance.main_generation
        )
        instance.pokedexes = validated_data.get("pokedexes", instance.pokedexes)
        instance.version_groups = validated_data.get(
            "version_groups", instance.version_groups
        )
        instance.save()
        return instance
