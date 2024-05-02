# Imports
from rest_framework import serializers
from apps.utilities.serializers import (
    VerboseEffectSerializer,
    MachineVersionDetailSerializer,
    NameSerializer,
    NamedAPIResourceSerializer,
    DescriptionSerializer,
    APIResourceSerializer,
    EffectSerializer,
)
from apps.moves.models import (
    MoveRoute,
    Move,
    MoveAilmentRoute,
    MoveAilment,
    MoveBattleStyleRoute,
    MoveBattleStyle,
    MoveCategoryRoute,
    MoveCategory,
    MoveDamageClassRoute,
    MoveDamageClass,
    MoveLearnMethodRoute,
    MoveLearnMethod,
    MoveTargetRoute,
    MoveTarget,
)


# Serializer for MoveRoute
class MoveRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new MoveRoute
    def create(self, validated_data):
        return MoveRoute.objects.create(**validated_data)

    # Method to update a MoveRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for PastMoveStatValue
class PastMoveStatValueSerializer(serializers.Serializer):
    # Fields
    accuracy = serializers.IntegerField(required=True)
    effect_chance = serializers.IntegerField(required=True)
    power = serializers.IntegerField(required=True)
    pp = serializers.IntegerField(required=True)
    effect_entries = VerboseEffectSerializer(many=True)
    type = NamedAPIResourceSerializer()
    version_group = NamedAPIResourceSerializer()


# Serializer for MoveStatChange
class MoveStatChangeSerializer(serializers.Serializer):
    # Fields
    change = serializers.IntegerField(required=True)
    stat = NamedAPIResourceSerializer()


# Serializer for MoveMetaData
class MoveMetaDataSerializer(serializers.Serializer):
    # Fields
    ailment = NamedAPIResourceSerializer()
    category = NamedAPIResourceSerializer()
    min_hits = serializers.IntegerField(required=True)
    max_hits = serializers.IntegerField(required=True)
    min_turns = serializers.IntegerField(required=True)
    max_turns = serializers.IntegerField(required=True)
    drain = serializers.IntegerField(required=True)
    healing = serializers.IntegerField(required=True)
    crit_rate = serializers.IntegerField(required=True)
    ailment_chance = serializers.IntegerField(required=True)
    flinch_chance = serializers.IntegerField(required=True)
    stat_chance = serializers.IntegerField(required=True)


# Serializer for MoveFlavorText
class MoveFlavorTextSerializer(serializers.Serializer):
    # Fields
    flavor_text = serializers.CharField(max_length=100, required=True)
    language = NamedAPIResourceSerializer()
    version_group = NamedAPIResourceSerializer()


# Serializer for ContestComboDetail
class ContestComboDetailSerializer(serializers.Serializer):
    # Fields
    use_before = NamedAPIResourceSerializer(many=True)
    use_after = NamedAPIResourceSerializer(many=True)


# Serializer for ContestComboSets
class ContestComboSetsSerializer(serializers.Serializer):
    # Fields
    normal = ContestComboDetailSerializer()
    super = ContestComboDetailSerializer()


# Serializer for AbilityEffectChange
class AbilityEffectChangeSerializer(serializers.Serializer):
    # Fields
    effect_entries = EffectSerializer(many=True)
    version_group = NamedAPIResourceSerializer()


# Serializer for Move
class MoveSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True, min_value=1)
    name = serializers.CharField(max_length=100, required=True)
    accuracy = serializers.IntegerField(required=True)
    effect_chance = serializers.IntegerField(required=True)
    pp = serializers.IntegerField(required=True)
    priority = serializers.IntegerField(required=True)
    power = serializers.IntegerField(required=True)
    contest_combos = ContestComboSetsSerializer()
    contest_effect = APIResourceSerializer()
    contest_type = NamedAPIResourceSerializer()
    damage_class = NamedAPIResourceSerializer()
    effect_entries = VerboseEffectSerializer(many=True)
    effect_changes = AbilityEffectChangeSerializer(many=True)
    learned_by_pokemon = NamedAPIResourceSerializer(many=True)
    flavor_text_entries = MoveFlavorTextSerializer(many=True)
    generation = NamedAPIResourceSerializer()
    machines = MachineVersionDetailSerializer(many=True)
    meta_data = MoveMetaDataSerializer()
    names = NameSerializer(many=True)
    past_values = PastMoveStatValueSerializer(many=True)
    stat_changes = MoveStatChangeSerializer(many=True)
    super_contest_effect = APIResourceSerializer()
    target = NamedAPIResourceSerializer()
    type = NamedAPIResourceSerializer()

    # Method to create a new Move
    def create(self, validated_data):
        return Move.objects.create(**validated_data)

    # Method to update a Move
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.accuracy = validated_data.get("accuracy", instance.accuracy)
        instance.effect_chance = validated_data.get(
            "effect_chance", instance.effect_chance
        )
        instance.pp = validated_data.get("pp", instance.pp)
        instance.priority = validated_data.get("priority", instance.priority)
        instance.power = validated_data.get("power", instance.power)
        instance.contest_combos = validated_data.get(
            "contest_combos", instance.contest_combos
        )
        instance.contest_effect = validated_data.get(
            "contest_effect", instance.contest_effect
        )
        instance.damage_class = validated_data.get(
            "damage_class", instance.damage_class
        )
        instance.effect_entries = validated_data.get(
            "effect_entries", instance.effect_entries
        )
        instance.effect_changes = validated_data.get(
            "effect_changes", instance.effect_changes
        )
        instance.flavor_text_entries = validated_data.get(
            "flavor_text_entries", instance.flavor_text_entries
        )
        instance.generation = validated_data.get("generation", instance.generation)
        instance.machines = validated_data.get("machines", instance.machines)
        instance.meta_data = validated_data.get("meta_data", instance.meta_data)
        instance.names = validated_data.get("names", instance.names)
        instance.past_values = validated_data.get("past_values", instance.past_values)
        instance.stat_changes = validated_data.get(
            "stat_changes", instance.stat_changes
        )
        instance.super_contest_effect = validated_data.get(
            "super_contest_effect", instance.super_contest_effect
        )
        instance.target = validated_data.get("target", instance.target)
        instance.type = validated_data.get("type", instance.type)
        instance.save()
        return instance


# Model for MoveAilmentRoute
class MoveAilmentRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new MoveAilmentRoute
    def create(self, validated_data):
        return MoveAilmentRoute.objects.create(**validated_data)

    # Method to update a MoveAilmentRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Model for MoveAilment
class MoveAilmentSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True, min_value=1)
    name = serializers.CharField(max_length=100, required=True)
    moves = NamedAPIResourceSerializer(many=True)
    names = NameSerializer(many=True)

    # Method to create a new MoveAilment
    def create(self, validated_data):
        return MoveAilment.objects.create(**validated_data)

    # Method to update a MoveAilment
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.moves = validated_data.get("moves", instance.moves)
        instance.name = validated_data.get("name", instance.name)
        instance.names = validated_data.get("names", instance.names)
        instance.save()


# Model for MoveBattleStyleRoute
class MoveBattleStyleRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new MoveBattleStyleRoute
    def create(self, validated_data):
        return MoveBattleStyleRoute.objects.create(**validated_data)

    # Method to update a MoveBattleStyleRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Model for MoveBattleStyle
class MoveBattleStyleSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True, min_value=1)
    name = serializers.CharField(max_length=100, required=True)
    names = NameSerializer(many=True)

    # Method to create a new MoveBattleStyle
    def create(self, validated_data):
        return MoveBattleStyle.objects.create(**validated_data)

    # Method to update a MoveBattleStyle
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.names = validated_data.get("names", instance.names)
        instance.save()
        return instance


# Model for MoveCategoryRoute
class MoveCategoryRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new MoveCategoryRoute
    def create(self, validated_data):
        return MoveCategoryRoute.objects.create(**validated_data)

    # Method to update a MoveCategoryRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Model for MoveCategory
class MoveCategorySerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True, min_value=1)
    name = serializers.CharField(max_length=100, required=True)
    moves = NamedAPIResourceSerializer(many=True)
    descriptions = DescriptionSerializer(many=True)

    # Method to create a new MoveCategory
    def create(self, validated_data):
        return MoveCategory.objects.create(**validated_data)

    # Method to update a MoveCategory
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.moves = validated_data.get("moves", instance.moves)
        instance.descriptions = validated_data.get(
            "descriptions", instance.descriptions
        )
        instance.save()
        return instance


# Model for MoveDamageClassRoute
class MoveDamageClassRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new MoveDamageClassRoute
    def create(self, validated_data):
        return MoveDamageClassRoute.objects.create(**validated_data)

    # Method to update a MoveDamageClassRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Model for MoveDamageClass
class MoveDamageClassSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True, min_value=1)
    name = serializers.CharField(max_length=100, required=True)
    descriptions = DescriptionSerializer(many=True)
    moves = NamedAPIResourceSerializer(many=True)
    names = NameSerializer(many=True)

    # Method to create a new MoveDamageClass
    def create(self, validated_data):
        return MoveDamageClass.objects.create(**validated_data)

    # Method to update a MoveDamageClass
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.descriptions = validated_data.get(
            "descriptions", instance.descriptions
        )
        instance.moves = validated_data.get("moves", instance.moves)
        instance.names = validated_data.get("names", instance.names)
        instance.save()
        return instance


# Model for MoveLearnMethodRoute
class MoveLearnMethodRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new MoveLearnMethodRoute
    def create(self, validated_data):
        return MoveLearnMethodRoute.objects.create(**validated_data)

    # Method to update a MoveLearnMethodRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Model for MoveLearnMethod
class MoveLearnMethodSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True, min_value=1)
    name = serializers.CharField(max_length=100, required=True)
    descriptions = DescriptionSerializer(many=True)
    names = NameSerializer(many=True)
    version_groups = NamedAPIResourceSerializer(many=True)

    # Method to create a new MoveLearnMethod
    def create(self, validated_data):
        return MoveLearnMethod.objects.create(**validated_data)

    # Method to update a MoveLearnMethod
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.name = validated_data.get("name", instance.name)
        instance.descriptions = validated_data.get(
            "descriptions", instance.descriptions
        )
        instance.names = validated_data.get("names", instance.names)
        instance.version_groups = validated_data.get(
            "version_groups", instance.version_groups
        )
        instance.save()
        return instance


# Serializer for MoveTargetRoute
class MoveTargetRouteSerializer(serializers.Serializer):
    # Fields
    name = serializers.CharField(max_length=100, required=True)
    url = serializers.CharField(max_length=100, required=True)

    # Method to create a new MoveTargetRoute
    def create(self, validated_data):
        return MoveTargetRoute.objects.create(**validated_data)

    # Method to update a MoveTargetRoute
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


# Serializer for MoveTarget
class MoveTargetSerializer(serializers.Serializer):
    # Fields
    entity_id = serializers.IntegerField(required=True, min_value=1)
    name = serializers.CharField(max_length=100, required=True)
    descriptions = DescriptionSerializer(many=True)
    moves = NamedAPIResourceSerializer(many=True)
    names = NameSerializer(many=True)

    # Method to create a new MoveTarget
    def create(self, validated_data):
        return MoveTarget.objects.create(**validated_data)

    # Method to update a MoveTarget
    def update(self, instance, validated_data):
        instance.entity_id = validated_data.get("entity_id", instance.entity_id)
        instance.descriptions = validated_data.get(
            "descriptions", instance.descriptions
        )
        instance.moves = validated_data.get("moves", instance.moves)
        instance.name = validated_data.get("name", instance.name)
        instance.names = validated_data.get("names", instance.names)
        instance.save()
        return instance
