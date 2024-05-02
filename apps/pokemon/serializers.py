# Imports
from rest_framework import serializers
from apps.utilities.serializers import (
    APIResourceSerializer,
    NamedAPIResourceSerializer,
    EffectSerializer,
    NameSerializer,
    VerboseEffectSerializer,
    DescriptionSerializer,
    VersionGameIndexSerializer,
    FlavorTextSerializer,
    GenerationGameIndexSerializer
)
from apps.pokemon.models import (
    AbilityRoute,
    Ability,
    CharacteristicRoute,
    Characteristic,
    EggGroupRoute,
    EggGroup,
    GenderRoute,
    Gender,
    GrowthRateRoute,
    GrowthRate,
    NatureRoute,
    Nature,
    PokeathlonStatRoute,
    PokeathlonStat,
    PokemonRoute,
    Pokemon,
    PokemonColorRoute,
    PokemonColor,
    PokemonFormRoute,
    PokemonForm,
    PokemonHabitatRoute,
    PokemonHabitat,
    PokemonShapeRoute,
    PokemonShape,
    PokemonSpeciesRoute,
    PokemonSpecies,
    StatRoute,
    Stat,
    TypeRoute,
    Type,
)


# Serializers for AbilityRoute
class AbilityRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField()
    url = serializers.CharField()

    # Method to create a new AbilityRoute
    def create(self, validated_data):
        return AbilityRoute.objects.create(**validated_data)

    # Method to update an AbilityRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for AbilityPokemon
class AbilityPokemonSerializer(serializers.Serializer):
    # Fields
    is_hidden = serializers.BooleanField()
    slot = serializers.IntegerField()
    pokemon = NamedAPIResourceSerializer()


# Serializer for AbilityFlavorText
class AbilityFlavorTextSerializer(serializers.Serializer):
    # Fields
    flavor_text = serializers.CharField()
    language = NamedAPIResourceSerializer()
    version_group = NamedAPIResourceSerializer()


# Serializer for AbilityEffectChange
class AbilityEffectChangeSerializer(serializers.Serializer):
    # Fields
    effect_entries = EffectSerializer(many=True)
    version_group = NamedAPIResourceSerializer()


# Serializer for Ability
class AbilitySerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField()
    name = serializers.CharField()
    is_main_series = serializers.BooleanField()
    generation = NamedAPIResourceSerializer()
    names = NameSerializer(many=True)
    effect_entries = VerboseEffectSerializer(many=True)
    effect_changes = AbilityEffectChangeSerializer(many=True)
    flavor_text_entries = AbilityFlavorTextSerializer(many=True)
    pokemon = AbilityPokemonSerializer(many=True)

    # Method to create a new Ability
    def create(self, validated_data):
        return Ability.objects.create(**validated_data)

    # Method to update an Ability
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.is_main_series = validated_data.get(
            "is_main_series", instance.is_main_series
        )
        instance.generation = validated_data.get("generation", instance.generation)
        instance.names = validated_data.get("names", instance.names)
        instance.effect_entries = validated_data.get(
            "effect_entries", instance.effect_entries
        )
        instance.effect_changes = validated_data.get(
            "effect_changes", instance.effect_changes
        )
        instance.flavor_text_entries = validated_data.get(
            "flavor_text_entries", instance.flavor_text_entries
        )
        instance.pokemon = validated_data.get("pokemon", instance.pokemon)
        instance.save()
        return instance


# Serializers for CharacteristicRoute
class CharacteristicRouteSerializer(serializers.Serializer):
    # Fields
    url = serializers.CharField()

    # Method to create a new CharacteristicRoute
    def create(self, validated_data):
        return CharacteristicRoute.objects.create(**validated_data)

    # Method to update a CharacteristicRoute
    def update(self, instance, validated_data):
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for Characteristic
class CharacteristicSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField()
    gene_modulo = serializers.IntegerField()
    possible_values = serializers.ListField(child=serializers.IntegerField())
    highest_stat = NamedAPIResourceSerializer()
    descriptions = DescriptionSerializer(many=True)

    # Method to create a new Characteristic
    def create(self, validated_data):
        return Characteristic.objects.create(**validated_data)

    # Method to update a Characteristic
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.gene_modulo = validated_data.get("gene_modulo", instance.gene_modulo)
        instance.possible_values = validated_data.get(
            "possible_values", instance.possible_values
        )
        instance.highest_stat = validated_data.get(
            "highest_stat", instance.highest_stat
        )
        instance.descriptions = validated_data.get(
            "descriptions", instance.descriptions
        )
        instance.save()
        return instance


# Serializers for EggGroupRoute
class EggGroupRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField()
    url = serializers.CharField()

    # Method to create a new EggGroupRoute
    def create(self, validated_data):
        return EggGroupRoute.objects.create(**validated_data)

    # Method to update an EggGroupRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for EggGroup
class EggGroupSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField()
    name = serializers.CharField()
    names = NameSerializer(many=True)
    pokemon_species = NamedAPIResourceSerializer(many=True)

    # Method to create a new EggGroup
    def create(self, validated_data):
        return EggGroup.objects.create(**validated_data)

    # Method to update an EggGroup
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.names = validated_data.get("names", instance.names)
        instance.pokemon_species = validated_data.get(
            "pokemon_species", instance.pokemon_species
        )
        instance.save()
        return instance


# Serializer for GenderRoute
class GenderRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField()
    url = serializers.CharField()

    # Method to create a new GenderRoute
    def create(self, validated_data):
        return GenderRoute.objects.create(**validated_data)

    # Method to update a GenderRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for PokemonSpeciesGender
class PokemonSpeciesGenderSerializer(serializers.Serializer):
    # Fields
    rate = serializers.IntegerField()
    pokemon_species = NamedAPIResourceSerializer()


# Serializer for Gender
class GenderSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField()
    name = serializers.CharField()
    pokemon_species_details = PokemonSpeciesGenderSerializer(many=True)
    required_for_evolution = NamedAPIResourceSerializer(many=True)

    # Method to create a new Gender
    def create(self, validated_data):
        return Gender.objects.create(**validated_data)

    # Method to update a Gender
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializers for GrowthRateRoute
class GrowthRateRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField()
    url = serializers.CharField()

    # Method to create a new GrowthRateRoute
    def create(self, validated_data):
        return GrowthRateRoute.objects.create(**validated_data)

    # Method to update a GrowthRateRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for GrowthRateExperienceLevel
class GrowthRateExperienceLevelSerializer(serializers.Serializer):
    # Fields
    level = serializers.IntegerField()
    experience = serializers.IntegerField()


# Serializer for GrowthRate
class GrowthRateSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField()
    name = serializers.CharField()
    formula = serializers.CharField()
    descriptions = DescriptionSerializer(many=True)
    levels = GrowthRateExperienceLevelSerializer(many=True)
    pokemon_species = NamedAPIResourceSerializer(many=True)

    # Method to create a new GrowthRate
    def create(self, validated_data):
        return GrowthRate.objects.create(**validated_data)

    # Method to update a GrowthRate
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.formula = validated_data.get("formula", instance.formula)
        instance.descriptions = validated_data.get(
            "descriptions", instance.descriptions
        )
        instance.levels = validated_data.get("levels", instance.levels)
        instance.pokemon_species = validated_data.get(
            "pokemon_species", instance.pokemon_species
        )
        instance.save()
        return instance


# Serializers for NatureRoute
class NatureRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField()
    url = serializers.CharField()

    # Method to create a new NatureRoute
    def create(self, validated_data):
        return NatureRoute.objects.create(**validated_data)

    # Method to update a NatureRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for MoveBattleStylePreference
class MoveBattleStylePreferenceSerializer(serializers.Serializer):
    # Fields
    low_hp_preference = serializers.IntegerField()
    high_hp_preference = serializers.IntegerField()
    move_battle_style = NamedAPIResourceSerializer()


# Serializer for NatureStatChange
class NatureStatChangeSerializer(serializers.Serializer):
    # Fields
    max_change = serializers.IntegerField()
    pokeathlon_stat = NamedAPIResourceSerializer()


# Serializer for Nature
class NatureSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField()
    name = serializers.CharField()
    decreased_stat = NamedAPIResourceSerializer()
    increased_stat = NamedAPIResourceSerializer()
    hates_flavor = NamedAPIResourceSerializer()
    likes_flavor = NamedAPIResourceSerializer()
    pokeathlon_stat_changes = NatureStatChangeSerializer(many=True)
    move_battle_style_preferences = MoveBattleStylePreferenceSerializer(many=True)
    names = NameSerializer(many=True)

    # Method to create a new Nature
    def create(self, validated_data):
        return Nature.objects.create(**validated_data)

    # Method to update a Nature
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.decreased_stat = validated_data.get(
            "decreased_stat", instance.decreased_stat
        )
        instance.increased_stat = validated_data.get(
            "increased_stat", instance.increased_stat
        )
        instance.hates_flavor = validated_data.get(
            "hates_flavor", instance.hates_flavor
        )
        instance.likes_flavor = validated_data.get(
            "likes_flavor", instance.likes_flavor
        )
        instance.pokeathlon_stat_changes = validated_data.get(
            "pokeathlon_stat_changes", instance.pokeathlon_stat_changes
        )
        instance.move_battle_style_preferences = validated_data.get(
            "move_battle_style_preferences", instance.move_battle_style_preferences
        )
        instance.names = validated_data.get("names", instance.names)
        instance.save()
        return instance


# Serializers for PokeathlonStatRoute
class PokeathlonStatRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField()
    url = serializers.CharField()

    # Method to create a new PokeathlonStatRoute
    def create(self, validated_data):
        return PokeathlonStatRoute.objects.create(**validated_data)

    # Method to update a PokeathlonStatRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for NaturePokeathlonStatAffect
class NaturePokeathlonStatAffectSerializer(serializers.Serializer):
    # Fields
    max_change = serializers.IntegerField()
    nature = NamedAPIResourceSerializer()


# Serializer for NaturePokeathlonStatAffectSets
class NaturePokeathlonStatAffectSetsSerializer(serializers.Serializer):
    # Fields
    increase = NaturePokeathlonStatAffectSerializer(many=True)
    decrease = NaturePokeathlonStatAffectSerializer(many=True)


# Serializer for PokeathlonStat
class PokeathlonStatSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField()
    name = serializers.CharField()
    names = NameSerializer(many=True)
    affecting_natures = NaturePokeathlonStatAffectSetsSerializer()

    # Method to create a new PokeathlonStat
    def create(self, validated_data):
        return PokeathlonStat.objects.create(**validated_data)

    # Method to update a PokeathlonStat
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.names = validated_data.get("names", instance.names)
        instance.affecting_natures = validated_data.get(
            "affecting_natures", instance.affecting_natures
        )
        instance.save()
        return instance


# Serializers for PokemonRoute
class PokemonRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField()
    url = serializers.CharField()

    # Method to create a new PokemonRoute
    def create(self, validated_data):
        return PokemonRoute.objects.create(**validated_data)

    # Method to update a PokemonRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for PokemonCries
class PokemonCriesSerializer(serializers.Serializer):
    # Fields
    latest = serializers.CharField()
    legacy = serializers.CharField()


# Serializer for PokemonSprites
class PokemonSpritesSerializer(serializers.Serializer):
    # Fields
    front_default = serializers.CharField()
    front_shiny = serializers.CharField()
    front_female = serializers.CharField()
    front_shiny_female = serializers.CharField()
    back_default = serializers.CharField()
    back_shiny = serializers.CharField
    back_female = serializers.CharField()
    back_shiny_female = serializers.CharField()
    other = serializers.DictField()
    versions = serializers.DictField()


# Serializer for PokemonStat
class PokemonStatSerializer(serializers.Serializer):
    # Fields
    base_stat = serializers.IntegerField()
    effort = serializers.IntegerField()
    stat = NamedAPIResourceSerializer()


# Serializer for PokemonMoveVersion
class PokemonMoveVersionSerializer(serializers.Serializer):
    # Fields
    move_learn_method = NamedAPIResourceSerializer()
    version_group = NamedAPIResourceSerializer()
    level_learned_at = serializers.IntegerField()


# Serializer for PokemonMove
class PokemonMoveSerializer(serializers.Serializer):
    # Fields
    move = NamedAPIResourceSerializer()
    version_group_details = PokemonMoveVersionSerializer(many=True)


# Serializer for PokemonHeldItemVersion
class PokemonHeldItemVersionSerializer(serializers.Serializer):
    # Fields
    version = NamedAPIResourceSerializer()
    rarity = serializers.IntegerField()


# Serializer for PokemonHeldItem
class PokemonHeldItemSerializer(serializers.Serializer):
    # Fields
    item = NamedAPIResourceSerializer()
    version_details = PokemonHeldItemVersionSerializer(many=True)


# Serializer for PokemonType
class PokemonTypeSerializer(serializers.Serializer):
    # Fields
    slot = serializers.IntegerField()
    type = NamedAPIResourceSerializer()


# Serializer for PokemonFormType
class PokemonFormTypeSerializer(serializers.Serializer):
    # Fields
    slot = serializers.IntegerField()
    type = NamedAPIResourceSerializer()


# Serializer for PokemonTypePast
class PokemonTypePastSerializer(serializers.Serializer):
    # Fields
    generation = NamedAPIResourceSerializer()
    types = PokemonTypeSerializer(many=True)


# Serializer for PokemonAbility
class PokemonAbilitySerializer(serializers.Serializer):
    # Fields
    is_hidden = serializers.BooleanField()
    slot = serializers.IntegerField()
    ability = NamedAPIResourceSerializer()


# Serializer for Pokemon
class PokemonSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField()
    name = serializers.CharField()
    base_experience = serializers.IntegerField()
    height = serializers.IntegerField()
    is_default = serializers.BooleanField()
    order = serializers.IntegerField()
    weight = serializers.IntegerField()
    abilities = PokemonAbilitySerializer(many=True)
    forms = NamedAPIResourceSerializer(many=True)
    game_indices = VersionGameIndexSerializer(many=True)
    held_items = PokemonHeldItemSerializer(many=True)
    moves = PokemonMoveSerializer(many=True)
    past_types = PokemonTypePastSerializer(many=True)
    sprites = PokemonSpritesSerializer()
    species = NamedAPIResourceSerializer()
    cries = PokemonCriesSerializer()
    species = NamedAPIResourceSerializer()
    stats = PokemonStatSerializer(many=True)
    types = PokemonTypeSerializer(many=True)

    # Method to create a new Pokemon
    def create(self, validated_data):
        return Pokemon.objects.create(**validated_data)

    # Method to update a Pokemon
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.base_experience = validated_data.get(
            "base_experience", instance.base_experience
        )
        instance.height = validated_data.get("height", instance.height)
        instance.is_default = validated_data.get("is_default", instance.is_default)
        instance.order = validated_data.get("order", instance.order)
        instance.weight = validated_data.get("weight", instance.weight)
        instance.abilities = validated_data.get("abilities", instance.abilities)
        instance.forms = validated_data.get("forms", instance.forms)
        instance.game_indices = validated_data.get(
            "game_indices", instance.game_indices
        )
        instance.held_items = validated_data.get("held_items", instance.held_items)
        instance.moves = validated_data.get("moves", instance.moves)
        instance.past_types = validated_data.get("past_types", instance.past_types)
        instance.sprites = validated_data.get("sprites", instance.sprites)
        instance.species = validated_data.get("species", instance.species)
        instance.cries = validated_data.get("cries", instance.cries)
        instance.species = validated_data.get("species", instance.species)
        instance.stats = validated_data.get("stats", instance.stats)
        instance.types = validated_data.get("types", instance.types)
        instance.save()
        return instance


# Serializers for PokemonColorRoute
class PokemonColorRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField()
    url = serializers.CharField()

    # Method to create a new PokemonColorRoute
    def create(self, validated_data):
        return PokemonColorRoute.objects.create(**validated_data)

    # Method to update a PokemonColorRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for PokemonColor
class PokemonColorSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField()
    name = serializers.CharField()
    names = NameSerializer(many=True)
    pokemon_species = NamedAPIResourceSerializer(many=True)

    # Method to create a new PokemonColor
    def create(self, validated_data):
        return PokemonColor.objects.create(**validated_data)

    # Method to update a PokemonColor
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.names = validated_data.get("names", instance.names)
        instance.pokemon_species = validated_data.get(
            "pokemon_species", instance.pokemon_species
        )
        instance.save()
        return instance


# Serializers for PokemonFormRoute
class PokemonFormRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField()
    url = serializers.CharField()

    # Method to create a new PokemonFormRoute
    def create(self, validated_data):
        return PokemonFormRoute.objects.create(**validated_data)

    # Method to update a PokemonFormRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for PokemonFormSprites
class PokemonFormSpritesSerializer(serializers.Serializer):
    # Fields
    front_default = serializers.CharField()
    front_shiny = serializers.CharField()
    back_default = serializers.CharField()
    back_shiny = serializers.CharField()


# Serializer for PokemonForm
class PokemonFormSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField()
    name = serializers.CharField()
    order = serializers.IntegerField()
    form_order = serializers.IntegerField()
    is_default = serializers.BooleanField()
    is_battle_only = serializers.BooleanField()
    is_mega = serializers.BooleanField()
    form_name = serializers.CharField()
    pokemon = NamedAPIResourceSerializer()
    types = PokemonFormTypeSerializer(many=True)
    sprites = PokemonFormSpritesSerializer()
    version_group = NamedAPIResourceSerializer()
    names = NameSerializer(many=True)
    form_names = NameSerializer(many=True)

    # Method to create a new PokemonForm
    def create(self, validated_data):
        return PokemonForm.objects.create(**validated_data)

    # Method to update a PokemonForm
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.order = validated_data.get("order", instance.order)
        instance.form_order = validated_data.get("form_order", instance.form_order)
        instance.is_default = validated_data.get("is_default", instance.is_default)
        instance.is_battle_only = validated_data.get(
            "is_battle_only", instance.is_battle_only
        )
        instance.is_mega = validated_data.get("is_mega", instance.is_mega)
        instance.form_name = validated_data.get("form_name", instance.form_name)
        instance.pokemon = validated_data.get("pokemon", instance.pokemon)
        instance.types = validated_data.get("types", instance.types)
        instance.sprites = validated_data.get("sprites", instance.sprites)
        instance.version_group = validated_data.get(
            "version_group", instance.version_group
        )
        instance.names = validated_data.get("names", instance.names)
        instance.form_names = validated_data.get("form_names", instance.form_names)
        instance.save()
        return instance


# Serializers for PokemonHabitatRoute
class PokemonHabitatRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField()
    url = serializers.CharField()

    # Method to create a new PokemonHabitatRoute
    def create(self, validated_data):
        return PokemonHabitatRoute.objects.create(**validated_data)

    # Method to update a PokemonHabitatRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for PokemonHabitat
class PokemonHabitatSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField()
    name = serializers.CharField()
    names = NameSerializer(many=True)
    pokemon_species = NamedAPIResourceSerializer(many=True)

    # Method to create a new PokemonHabitat
    def create(self, validated_data):
        return PokemonHabitat.objects.create(**validated_data)

    # Method to update a PokemonHabitat
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.names = validated_data.get("names", instance.names)
        instance.pokemon_species = validated_data.get(
            "pokemon_species", instance.pokemon_species
        )
        instance.save()
        return instance


# Serializers for PokemonShapeRoute
class PokemonShapeRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField()
    url = serializers.CharField()

    # Method to create a new PokemonShapeRoute
    def create(self, validated_data):
        return PokemonShapeRoute.objects.create(**validated_data)

    # Method to update a PokemonShapeRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for AwesomeName
class AwesomeNameSerializer(serializers.Serializer):
    # Fields
    awesome_name = serializers.CharField()
    language = NamedAPIResourceSerializer()


# Serializer for PokemonShape
class PokemonShapeSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField()
    name = serializers.CharField()
    awesome_names = AwesomeNameSerializer(many=True)
    names = NameSerializer(many=True)
    pokemon_species = NamedAPIResourceSerializer(many=True)

    # Method to create a new PokemonShape
    def create(self, validated_data):
        return PokemonShape.objects.create(**validated_data)

    # Method to update a PokemonShape
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.awesome_names = validated_data.get(
            "awesome_names", instance.awesome_names
        )
        instance.names = validated_data.get("names", instance.names)
        instance.pokemon_species = validated_data.get(
            "pokemon_species", instance.pokemon_species
        )
        instance.save()
        return instance


# Serializers for PokemonSpeciesRoute
class PokemonSpeciesRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField()
    url = serializers.CharField()

    # Method to create a new PokemonSpeciesRoute
    def create(self, validated_data):
        return PokemonSpeciesRoute.objects.create(**validated_data)

    # Method to update a PokemonSpeciesRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for PokemonSpeciesVariety
class PokemonSpeciesVarietySerializer(serializers.Serializer):
    # Fields
    is_default = serializers.BooleanField()
    pokemon = NamedAPIResourceSerializer()


# Serializer for PalParkEncounterArea
class PalParkEncounterAreaSerializer(serializers.Serializer):
    # Fields
    base_score = serializers.IntegerField()
    rate = serializers.IntegerField()
    area = NamedAPIResourceSerializer()


# Serializer for PokemonSpeciesDexEntry
class PokemonSpeciesDexEntrySerializer(serializers.Serializer):
    # Fields
    entry_number = serializers.IntegerField()
    pokedex = NamedAPIResourceSerializer()


# Serializer for Genus
class GenusSerializer(serializers.Serializer):
    # Fields
    genus = serializers.CharField()
    language = NamedAPIResourceSerializer()


# Serializer for PokemonSpecies
class PokemonSpeciesSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField()
    name = serializers.CharField()
    order = serializers.IntegerField()
    gender_rate = serializers.IntegerField()
    capture_rate = serializers.IntegerField()
    base_happiness = serializers.IntegerField()
    is_baby = serializers.BooleanField()
    is_legendary = serializers.BooleanField()
    is_mythical = serializers.BooleanField()
    hatch_counter = serializers.IntegerField
    has_gender_differences = serializers.BooleanField()
    forms_switchable = serializers.BooleanField()
    growth_rate = NamedAPIResourceSerializer()
    pokedex_numbers = PokemonSpeciesDexEntrySerializer(many=True)
    egg_groups = NamedAPIResourceSerializer(many=True)
    color = NamedAPIResourceSerializer()
    shape = NamedAPIResourceSerializer()
    evolves_from_species = NamedAPIResourceSerializer()
    evolution_chain = APIResourceSerializer()
    habitat = NamedAPIResourceSerializer()
    generation = NamedAPIResourceSerializer()
    names = NameSerializer(many=True)
    pal_park_encounters = PalParkEncounterAreaSerializer(many=True)
    flavor_text_entries = FlavorTextSerializer(many=True)
    form_descriptions = DescriptionSerializer(many=True)
    genera = GenusSerializer(many=True)
    varieties = PokemonSpeciesVarietySerializer(many=True)

    # Method to create a new PokemonSpecies
    def create(self, validated_data):
        return PokemonSpecies.objects.create(**validated_data)

    # Method to update a PokemonSpecies
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.order = validated_data.get("order", instance.order)
        instance.gender_rate = validated_data.get("gender_rate", instance.gender_rate)
        instance.capture_rate = validated_data.get(
            "capture_rate", instance.capture_rate
        )
        instance.base_happiness = validated_data.get(
            "base_happiness", instance.base_happiness
        )
        instance.is_baby = validated_data.get("is_baby", instance.is_baby)
        instance.is_legendary = validated_data.get(
            "is_legendary", instance.is_legendary
        )
        instance.is_mythical = validated_data.get("is_mythical", instance.is_mythical)
        instance.hatch_counter = validated_data.get(
            "hatch_counter", instance.hatch_counter
        )
        instance.has_gender_differences = validated_data.get(
            "has_gender_differences", instance.has_gender_differences
        )
        instance.forms_switchable = validated_data.get(
            "forms_switchable", instance.forms_switchable
        )
        instance.growth_rate = validated_data.get("growth_rate", instance.growth_rate)
        instance.pokedex_numbers = validated_data.get(
            "pokedex_numbers", instance.pokedex_numbers
        )
        instance.egg_groups = validated_data.get("egg_groups", instance.egg_groups)
        instance.color = validated_data.get("color", instance.color)
        instance.shape = validated_data.get("shape", instance.shape)
        instance.evolves_from_species = validated_data.get(
            "evolves_from_species", instance.evolves_from_species
        )
        instance.evolution_chain = validated_data.get(
            "evolution_chain", instance.evolution_chain
        )
        instance.habitat = validated_data.get("habitat", instance.habitat)
        instance.generation = validated_data.get("generation", instance.generation)
        instance.names = validated_data.get("names", instance.names)
        instance.pal_park_encounters = validated_data.get(
            "pal_park_encounters", instance.pal_park_encounters
        )
        instance.flavor_text_entries = validated_data.get(
            "flavor_text_entries", instance.flavor_text_entries
        )
        instance.form_descriptions = validated_data.get(
            "form_descriptions", instance.form_descriptions
        )
        instance.genera = validated_data.get("genera", instance.genera)
        instance.varieties = validated_data.get("varieties", instance.varieties)
        instance.save()
        return instance


# Serializers for StatRoute
class StatRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField()
    url = serializers.CharField()

    # Method to create a new StatRoute
    def create(self, validated_data):
        return StatRoute.objects.create(**validated_data)

    # Method to update a StatRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for NatureStaAffectSets
class NatureStatAffectSetsSerializer(serializers.Serializer):
    # Fields
    increase = NamedAPIResourceSerializer(many=True)
    decrease = NamedAPIResourceSerializer(many=True)


# Serializer for MoveStatAffect
class MoveStatAffectSerializer(serializers.Serializer):
    # Fields
    change = serializers.IntegerField()
    move = NamedAPIResourceSerializer()


# Serializer for MoveStatAffectSets
class MoveStatAffectSetsSerializer(serializers.Serializer):
    # Fields
    increase = MoveStatAffectSerializer(many=True)
    decrease = MoveStatAffectSerializer(many=True)


# Serializer for Stat
class StatSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField()
    name = serializers.CharField()
    game_index = serializers.IntegerField()
    is_battle_only = serializers.BooleanField()
    affecting_moves = MoveStatAffectSetsSerializer()
    affecting_natures = NatureStatAffectSetsSerializer()
    characteristics = NamedAPIResourceSerializer(many=True)
    move_damage_class = NamedAPIResourceSerializer()
    names = NameSerializer(many=True)

    # Method to create a new Stat
    def create(self, validated_data):
        return Stat.objects.create(**validated_data)

    # Method to update a Stat
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.game_index = validated_data.get("game_index", instance.game_index)
        instance.is_battle_only = validated_data.get(
            "is_battle_only", instance.is_battle_only
        )
        instance.affecting_moves = validated_data.get(
            "affecting_moves", instance.affecting_moves
        )
        instance.affecting_natures = validated_data.get(
            "affecting_natures", instance.affecting_natures
        )
        instance.characteristics = validated_data.get(
            "characteristics", instance.characteristics
        )
        instance.move_damage_class = validated_data.get(
            "move_damage_class", instance.move_damage_class
        )
        instance.names = validated_data.get("names", instance.names)
        instance.save()
        return instance


# Serializers for TypeRoute
class TypeRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField()
    url = serializers.CharField()

    # Method to create a new TypeRoute
    def create(self, validated_data):
        return TypeRoute.objects.create(**validated_data)

    # Method to update a TypeRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for TypeRelations
class TypeRelationsSerializer(serializers.Serializer):
    # Fields
    no_damage_to = NamedAPIResourceSerializer(many=True)
    half_damage_to = NamedAPIResourceSerializer(many=True)
    double_damage_to = NamedAPIResourceSerializer(many=True)
    no_damage_from = NamedAPIResourceSerializer(many=True)
    half_damage_from = NamedAPIResourceSerializer(many=True)
    double_damage_from = NamedAPIResourceSerializer(many=True)


# Serializer for TypeRelationsPast
class TypeRelationsPastSerializer(serializers.Serializer):
    # Fields
    generation = NamedAPIResourceSerializer()
    damage_relations = TypeRelationsSerializer()



# Serializer for TypePokemon
class TypePokemonSerializer(serializers.Serializer):
    # Fields
    slot = serializers.IntegerField()
    pokemon = NamedAPIResourceSerializer()


# Serializer for Type
class TypeSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField()
    name = serializers.CharField()
    damage_relations = TypeRelationsSerializer()
    past_damage_relations = TypeRelationsSerializer(many=True)
    game_indices = GenerationGameIndexSerializer(many=True)
    generation = NamedAPIResourceSerializer()
    move_damage_class = NamedAPIResourceSerializer()
    names = NameSerializer(many=True)
    pokemon = TypePokemonSerializer(many=True)
    moves = NamedAPIResourceSerializer(many=True)

    # Method to create a new Type
    def create(self, validated_data):
        return Type.objects.create(**validated_data)

    # Method to update a Type
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.damage_relations = validated_data.get(
            "damage_relations", instance.damage_relations
        )
        instance.past_damage_relations = validated_data.get(
            "past_damage_relations", instance.past_damage_relations
        )
        instance.game_indices = validated_data.get(
            "game_indices", instance.game_indices
        )
        instance.generation = validated_data.get("generation", instance.generation)
        instance.move_damage_class = validated_data.get(
            "move_damage_class", instance.move_damage_class
        )
        instance.names = validated_data.get("names", instance.names)
        instance.pokemon = validated_data.get("pokemon", instance.pokemon)
        instance.past_types = validated_data.get("past_types", instance.past_types)
        instance.save()
        return instance
