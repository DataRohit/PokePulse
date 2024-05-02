# Imports
import json
from pathlib import Path
from tqdm import tqdm
from django.core.management.base import BaseCommand
from django.db import IntegrityError

# Models
from apps.base.models import BaseRoute
from apps.berries.models import (
    BerryRoute,
    Berry,
    BerryFirmnessRoute,
    BerryFirmness,
    BerryFlavorRoute,
    BerryFlavor,
)
from apps.contests.models import (
    ContestTypeRoute,
    ContestType,
    ContestEffectRoute,
    ContestEffect,
    SuperContestEffectRoute,
    SuperContestEffect,
)
from apps.encounters.models import (
    EncounterMethodRoute,
    EncounterMethod,
    EncounterConditionRoute,
    EncounterCondition,
    EncounterConditionValueRoute,
    EncounterConditionValue,
)
from apps.evolutions.models import (
    EvolutionChainRoute,
    EvolutionChain,
    EvolutionTriggerRoute,
    EvolutionTrigger,
)
from apps.games.models import (
    GenerationRoute,
    Generation,
    PokedexRoute,
    Pokedex,
    VersionRoute,
    Version,
    VersionGroupRoute,
    VersionGroup,
)
from apps.items.models import (
    ItemRoute,
    Item,
    ItemCategoryRoute,
    ItemCategory,
    ItemAttributeRoute,
    ItemAttribute,
    ItemFlingEffectRoute,
    ItemFlingEffect,
    ItemPocketRoute,
    ItemPocket,
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
from apps.machines.models import MachineRoute, Machine
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
from apps.utilities.models import LanguageRoute, Language


# Class for command
class Command(BaseCommand):
    # Help text
    help = "Load fixtures"

    # Model mapping
    model_mapping = {
        "BaseRoute": BaseRoute,
        "BerryRoute": BerryRoute,
        "Berry": Berry,
        "BerryFirmnessRoute": BerryFirmnessRoute,
        "BerryFirmness": BerryFirmness,
        "BerryFlavorRoute": BerryFlavorRoute,
        "BerryFlavor": BerryFlavor,
        "ContestTypeRoute": ContestTypeRoute,
        "ContestType": ContestType,
        "ContestEffectRoute": ContestEffectRoute,
        "ContestEffect": ContestEffect,
        "SuperContestEffectRoute": SuperContestEffectRoute,
        "SuperContestEffect": SuperContestEffect,
        "EncounterMethodRoute": EncounterMethodRoute,
        "EncounterMethod": EncounterMethod,
        "EncounterConditionRoute": EncounterConditionRoute,
        "EncounterCondition": EncounterCondition,
        "EncounterConditionValueRoute": EncounterConditionValueRoute,
        "EncounterConditionValue": EncounterConditionValue,
        "EvolutionChainRoute": EvolutionChainRoute,
        "EvolutionChain": EvolutionChain,
        "EvolutionTriggerRoute": EvolutionTriggerRoute,
        "EvolutionTrigger": EvolutionTrigger,
        "GenerationRoute": GenerationRoute,
        "Generation": Generation,
        "PokedexRoute": PokedexRoute,
        "Pokedex": Pokedex,
        "VersionRoute": VersionRoute,
        "Version": Version,
        "VersionGroupRoute": VersionGroupRoute,
        "VersionGroup": VersionGroup,
        "ItemRoute": ItemRoute,
        "Item": Item,
        "ItemCategoryRoute": ItemCategoryRoute,
        "ItemCategory": ItemCategory,
        "ItemAttributeRoute": ItemAttributeRoute,
        "ItemAttribute": ItemAttribute,
        "ItemFlingEffectRoute": ItemFlingEffectRoute,
        "ItemFlingEffect": ItemFlingEffect,
        "ItemPocketRoute": ItemPocketRoute,
        "ItemPocket": ItemPocket,
        "LocationRoute": LocationRoute,
        "Location": Location,
        "LocationAreaRoute": LocationAreaRoute,
        "LocationArea": LocationArea,
        "PalParkAreaRoute": PalParkAreaRoute,
        "PalParkArea": PalParkArea,
        "RegionRoute": RegionRoute,
        "Region": Region,
        "MachineRoute": MachineRoute,
        "Machine": Machine,
        "MoveRoute": MoveRoute,
        "Move": Move,
        "MoveAilmentRoute": MoveAilmentRoute,
        "MoveAilment": MoveAilment,
        "MoveBattleStyleRoute": MoveBattleStyleRoute,
        "MoveBattleStyle": MoveBattleStyle,
        "MoveCategoryRoute": MoveCategoryRoute,
        "MoveCategory": MoveCategory,
        "MoveDamageClassRoute": MoveDamageClassRoute,
        "MoveDamageClass": MoveDamageClass,
        "MoveLearnMethodRoute": MoveLearnMethodRoute,
        "MoveLearnMethod": MoveLearnMethod,
        "MoveTargetRoute": MoveTargetRoute,
        "MoveTarget": MoveTarget,
        "AbilityRoute": AbilityRoute,
        "Ability": Ability,
        "CharacteristicRoute": CharacteristicRoute,
        "Characteristic": Characteristic,
        "EggGroupRoute": EggGroupRoute,
        "EggGroup": EggGroup,
        "GenderRoute": GenderRoute,
        "Gender": Gender,
        "GrowthRateRoute": GrowthRateRoute,
        "GrowthRate": GrowthRate,
        "NatureRoute": NatureRoute,
        "Nature": Nature,
        "PokeathlonStatRoute": PokeathlonStatRoute,
        "PokeathlonStat": PokeathlonStat,
        "PokemonRoute": PokemonRoute,
        "Pokemon": Pokemon,
        "PokemonColorRoute": PokemonColorRoute,
        "PokemonColor": PokemonColor,
        "PokemonFormRoute": PokemonFormRoute,
        "PokemonForm": PokemonForm,
        "PokemonHabitatRoute": PokemonHabitatRoute,
        "PokemonHabitat": PokemonHabitat,
        "PokemonShapeRoute": PokemonShapeRoute,
        "PokemonShape": PokemonShape,
        "PokemonSpeciesRoute": PokemonSpeciesRoute,
        "PokemonSpecies": PokemonSpecies,
        "StatRoute": StatRoute,
        "Stat": Stat,
        "TypeRoute": TypeRoute,
        "Type": Type,
        "LanguageRoute": LanguageRoute,
        "Language": Language,
    }

    # Method to load the fixtures
    def handle(self, *args, **kwargs):
        # Get the list of fixtures
        fixture_dir = Path("apps/utilities/fixtures")
        fixture_files = list(fixture_dir.glob("*.json"))

        # Check if there are fixtures
        if not fixture_files:
            print("No fixture files found.")
            return

        try:
            # Add line break
            print()

            # Print the message
            self.stdout.write(
                self.style.SUCCESS(
                    f"Loading {len(fixture_files)} Fixtures Into MongoDB Database..."
                )
            )

            # Add line break
            print()

            # Traverse over the fixtures
            for fixture_path in fixture_files:
                # Get the fixture model name
                file_name = "".join(
                    [word.title() for word in fixture_path.stem.split("_")[:-1]]
                )

                # Get the model
                model = self.model_mapping.get(file_name)

                # Load the json file
                with open(fixture_path, "r") as file:
                    data = json.load(file)

                # List to store entries
                entries = []

                # Check if file is Route or not
                for item in tqdm(
                    data,
                    desc=f"Loading {file_name} Fixtures".ljust(50),
                    ncols=100,
                    bar_format="{desc}: {percentage:3.0f}% |{bar}| {n: >5} / {total: <5}",
                    ascii=" =",
                ):

                    # Create an entry and append to the list
                    entries.append(model(**item))

                # Bulk insert the entries
                model.objects.insert(entries)

            # Add line break
            print()

            # Print the message
            self.stdout.write(
                self.style.SUCCESS(
                    "Fixtures Successfully Loaded into MongoDB Database..."
                ),
            )

        # Handle the exceptions
        except IntegrityError as e:
            self.stderr.write(self.style.ERROR(f"IntegrityError: {e}"))
            self.stderr.write(self.style.ERROR("Fix the issue and try again."))
