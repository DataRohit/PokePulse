# Imports
from rest_framework import serializers
from apps.utilities.serializers import (
    NamedAPIResourceSerializer,
    NameSerializer,
    DescriptionSerializer,
)
from apps.games.models import (
    GenerationRoute,
    Generation,
    PokedexRoute,
    PokemonEntry,
    Pokedex,
    VersionRoute,
    Version,
    VersionGroupRoute,
    VersionGroup,
)


# Serializer for GenerationRoute
class GenerationRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new GenerationRoute
    def create(self, validated_data):
        return GenerationRoute.objects.create(**validated_data)

    # Method to update a GenerationRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for Generation
class GenerationSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=100, required=True)
    abilities = NamedAPIResourceSerializer(many=True, required=True)
    names = NameSerializer(many=True, required=True)
    main_region = NamedAPIResourceSerializer(required=True)
    moves = NamedAPIResourceSerializer(many=True, required=True)
    pokemon_species = NamedAPIResourceSerializer(many=True, required=True)
    types = NamedAPIResourceSerializer(many=True, required=True)
    version_groups = NamedAPIResourceSerializer(many=True, required=True)

    # Method to create a new Generation
    def create(self, validated_data):
        return Generation.objects.create(**validated_data)

    # Method to update a Generation
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.abilities = validated_data.get("abilities", instance.abilities)
        instance.names = validated_data.get("names", instance.names)
        instance.main_region = validated_data.get("main_region", instance.main_region)
        instance.moves = validated_data.get("moves", instance.moves)
        instance.pokemon_species = validated_data.get(
            "pokemon_species", instance.pokemon_species
        )
        instance.types = validated_data.get("types", instance.types)
        instance.version_groups = validated_data.get(
            "version_groups", instance.version_groups
        )
        instance.save()
        return instance


# Serializer for PokedexRoute
class PokedexRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new PokedexRoute
    def create(self, validated_data):
        return PokedexRoute.objects.create(**validated_data)

    # Method to update a PokedexRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for PokemonEntry
class PokemonEntrySerializer(serializers.Serializer):
    # Fields
    entry_number = serializers.IntegerField(required=True)
    pokemon_species = NamedAPIResourceSerializer(required=True)


# Serializer for Pokedex
class PokedexSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=100, required=True)
    is_main_series = serializers.BooleanField(required=True)
    descriptions = DescriptionSerializer(many=True, required=True)
    names = NameSerializer(many=True, required=True)
    pokemon_entries = PokemonEntrySerializer(many=True, required=True)
    region = NamedAPIResourceSerializer(required=True)
    version_groups = NamedAPIResourceSerializer(many=True, required=True)

    # Method to create a new Pokedex
    def create(self, validated_data):
        return Pokedex.objects.create(**validated_data)

    # Method to update a Pokedex
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.is_main_series = validated_data.get(
            "is_main_series", instance.is_main_series
        )
        instance.descriptions = validated_data.get(
            "descriptions", instance.descriptions
        )
        instance.names = validated_data.get("names", instance.names)
        instance.pokemon_entries = validated_data.get(
            "pokemon_entries", instance.pokemon_entries
        )
        instance.region = validated_data.get("region", instance.region)
        instance.version_groups = validated_data.get(
            "version_groups", instance.version_groups
        )
        instance.save()
        return instance


# Serializer for VersionRoute
class VersionRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new VersionRoute
    def create(self, validated_data):
        return VersionRoute.objects.create(**validated_data)

    # Method to update a VersionRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for Version
class VersionSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=100, required=True)
    names = NameSerializer(many=True, required=True)
    version_group = NamedAPIResourceSerializer(required=True)

    # Method to create a new Version
    def create(self, validated_data):
        return Version.objects.create(**validated_data)

    # Method to update a Version
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.names = validated_data.get("names", instance.names)
        instance.version_group = validated_data.get(
            "version_group", instance.version_group
        )
        instance.save()
        return instance


# Serializer for VersionGroupRoute
class VersionGroupRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new VersionGroupRoute
    def create(self, validated_data):
        return VersionGroupRoute.objects.create(**validated_data)

    # Method to update a VersionGroupRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for VersionGroup
class VersionGroupSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=100, required=True)
    order = serializers.IntegerField(required=True)
    generation = NamedAPIResourceSerializer(required=True)
    move_learn_methods = NamedAPIResourceSerializer(many=True, required=True)
    pokedexes = NamedAPIResourceSerializer(many=True, required=True)
    regions = NamedAPIResourceSerializer(many=True, required=True)
    versions = NamedAPIResourceSerializer(many=True, required=True)

    # Method to create a new VersionGroup
    def create(self, validated_data):
        return VersionGroup.objects.create(**validated_data)

    # Method to update a VersionGroup
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.order = validated_data.get("order", instance.order)
        instance.generation = validated_data.get("generation", instance.generation)
        instance.move_learn_methods = validated_data.get(
            "move_learn_methods", instance.move_learn_methods
        )
        instance.pokedexes = validated_data.get("pokedexes", instance.pokedexes)
        instance.regions = validated_data.get("regions", instance.regions)
        instance.versions = validated_data.get("versions", instance.versions)
        instance.save()
        return instance
