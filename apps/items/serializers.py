# Imports
from rest_framework import serializers
from apps.utilities.serializers import (
    APIResourceSerializer,
    NamedAPIResourceSerializer,
    NameSerializer,
    VerboseEffectSerializer,
    VersionGroupFlavorTextSerializer,
    GenerationGameIndexSerializer,
    MachineVersionDetailSerializer,
    DescriptionSerializer,
    EffectSerializer,
)
from apps.items.models import (
    ItemRoute,
    Item,
    ItemAttributeRoute,
    ItemAttribute,
    ItemCategoryRoute,
    ItemCategory,
    ItemFlingEffectRoute,
    ItemFlingEffect,
    ItemPocketRoute,
    ItemPocket,
)


# Serializer for ItemRoute
class ItemRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new ItemRoute
    def create(self, validated_data):
        return ItemRoute.objects.create(**validated_data)

    # Method to update a ItemRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for ItemHolderPokemonVersionDetail
class ItemHolderPokemonVersionDetailSerializer(serializers.Serializer):
    # Fields
    rarity = serializers.IntegerField(required=True)
    version = NamedAPIResourceSerializer(required=True)


# Serializer for ItemHolderPokemon
class ItemHolderPokemonSerializer(serializers.Serializer):
    # Fields
    pokemon = NamedAPIResourceSerializer(required=True)
    version_details = ItemHolderPokemonVersionDetailSerializer(many=True, required=True)


# Serializer for ItemSprites
class ItemSpritesSerializer(serializers.Serializer):
    # Fields
    default = serializers.CharField(max_length=100, required=True)


# Serializer for Item
class ItemSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=100, required=True)
    cost = serializers.IntegerField(required=True)
    fling_power = serializers.IntegerField(required=True)
    attributes = NamedAPIResourceSerializer(many=True, required=True)
    category = NamedAPIResourceSerializer(required=True)
    effect_entries = VerboseEffectSerializer(many=True, required=True)
    flavor_text_entries = VersionGroupFlavorTextSerializer(many=True, required=True)
    game_indices = GenerationGameIndexSerializer(many=True, required=True)
    names = NameSerializer(many=True, required=True)
    sprites = ItemSpritesSerializer(required=True)
    held_by_pokemon = ItemHolderPokemonSerializer(many=True, required=True)
    baby_trigger_for = APIResourceSerializer(required=True)
    machines = MachineVersionDetailSerializer(many=True, required=True)

    # Method to create a new Item
    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    # Method to update a Item
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.cost = validated_data.get("cost", instance.cost)
        instance.fling_power = validated_data.get("fling_power", instance.fling_power)
        instance.attributes = validated_data.get("attributes", instance.attributes)
        instance.category = validated_data.get("category", instance.category)
        instance.effect_entries = validated_data.get(
            "effect_entries", instance.effect_entries
        )
        instance.flavor_text_entries = validated_data.get(
            "flavor_text_entries", instance.flavor_text_entries
        )
        instance.game_indices = validated_data.get(
            "game_indices", instance.game_indices
        )
        instance.held_by_pokemon = validated_data.get(
            "held_by_pokemon", instance.held_by_pokemon
        )
        instance.sprites = validated_data.get("sprites", instance.sprites)
        instance.save()
        return instance


# Serializer for ItemAttributeRoute
class ItemAttributeRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new ItemAttributeRoute
    def create(self, validated_data):
        return ItemAttributeRoute.objects.create(**validated_data)

    # Method to update a ItemAttributeRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for ItemAttribute
class ItemAttributeSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=100, required=True)
    items = NamedAPIResourceSerializer(many=True, required=True)
    names = NameSerializer(many=True, required=True)
    descriptions = DescriptionSerializer(many=True, required=True)

    # Method to create a new ItemAttribute
    def create(self, validated_data):
        return ItemAttribute.objects.create(**validated_data)

    # Method to update a ItemAttribute
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.items = validated_data.get("items", instance.items)
        instance.names = validated_data.get("names", instance.names)
        instance.descriptions = validated_data.get(
            "descriptions", instance.descriptions
        )
        instance.save()
        return instance


# Serializer for ItemCategoryRoute
class ItemCategoryRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new ItemCategoryRoute
    def create(self, validated_data):
        return ItemCategoryRoute.objects.create(**validated_data)

    # Method to update a ItemCategoryRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for ItemCategory
class ItemCategorySerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=100, required=True)
    items = NamedAPIResourceSerializer(many=True, required=True)
    names = NameSerializer(many=True, required=True)
    pocket = NamedAPIResourceSerializer(required=True)

    # Method to create a new ItemCategory
    def create(self, validated_data):
        return ItemCategory.objects.create(**validated_data)

    # Method to update a ItemCategory
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.items = validated_data.get("items", instance.items)
        instance.names = validated_data.get("names", instance.names)
        instance.pocket = validated_data.get("pocket", instance.pocket)
        instance.save()
        return instance


# Model for ItemFlingEffectRoute
class ItemFlingEffectRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new ItemFlingEffectRoute
    def create(self, validated_data):
        return ItemFlingEffectRoute.objects.create(**validated_data)

    # Method to update a ItemFlingEffectRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for ItemFlingEffect
class ItemFlingEffectSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=100, required=True)
    effect_entries = EffectSerializer(many=True, required=True)
    items = NamedAPIResourceSerializer(many=True, required=True)

    # Method to create a new ItemFlingEffect
    def create(self, validated_data):
        return ItemFlingEffect.objects.create(**validated_data)

    # Method to update a ItemFlingEffect
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.effect_entries = validated_data.get(
            "effect_entries", instance.effect_entries
        )
        instance.items = validated_data.get("items", instance.items)
        instance.save()
        return instance


# Serializer for ItemPocketRoute
class ItemPocketRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new ItemPocketRoute
    def create(self, validated_data):
        return ItemPocketRoute.objects.create(**validated_data)

    # Method to update a ItemPocketRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for ItemPocket
class ItemPocketSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=100, required=True)
    categories = NamedAPIResourceSerializer(many=True, required=True)
    names = NameSerializer(many=True, required=True)

    # Method to create a new ItemPocket
    def create(self, validated_data):
        return ItemPocket.objects.create(**validated_data)

    # Method to update a ItemPocket
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.categories = validated_data.get("categories", instance.categories)
        instance.names = validated_data.get("names", instance.names)
        instance.save()
        return instance
