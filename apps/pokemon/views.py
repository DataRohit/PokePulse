# Imports
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
from apps.pokemon.serializers import (
    AbilityRouteSerializer,
    AbilitySerializer,
    CharacteristicRouteSerializer,
    CharacteristicSerializer,
    EggGroupRouteSerializer,
    EggGroupSerializer,
    GenderRouteSerializer,
    GenderSerializer,
    GrowthRateRouteSerializer,
    GrowthRateSerializer,
    NatureRouteSerializer,
    NatureSerializer,
    PokeathlonStatRouteSerializer,
    PokeathlonStatSerializer,
    PokemonRouteSerializer,
    PokemonSerializer,
    PokemonColorRouteSerializer,
    PokemonColorSerializer,
    PokemonFormRouteSerializer,
    PokemonFormSerializer,
    PokemonHabitatRouteSerializer,
    PokemonHabitatSerializer,
    PokemonShapeRouteSerializer,
    PokemonShapeSerializer,
    PokemonSpeciesRouteSerializer,
    PokemonSpeciesSerializer,
    StatRouteSerializer,
    StatSerializer,
    TypeRouteSerializer,
    TypeSerializer,
)
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# View to serve the ability routes
class AbilityRouteView(APIView):
    serializer_class = AbilityRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--ability-routes",
        operation_description="Get the ability routes",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            )
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Ability routes",
                schema=AbilityRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request):
        ability_routes = AbilityRoute.objects.all()
        serializer = AbilityRouteSerializer(ability_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the ability
class AbilitiesView(APIView):
    serializer_class = AbilitySerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--abilities",
        operation_description="Get the abilities",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            ),
            openapi.Parameter(
                name="entity_id",
                default=1,
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                required=True,
                description="The id of the ability",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Abilities",
                schema=AbilitySerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request, entity_id):
        abilities = Ability.objects.filter(entity_id=entity_id)
        serializer = AbilitySerializer(abilities, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the characteristic routes
class CharacteristicRouteView(APIView):
    serializer_class = CharacteristicRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--characteristic-routes",
        operation_description="Get the characteristic routes",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            )
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Characteristic routes",
                schema=CharacteristicRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request):
        characteristic_routes = CharacteristicRoute.objects.all()
        serializer = CharacteristicRouteSerializer(characteristic_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the characteristic
class CharacteristicsView(APIView):
    serializer_class = CharacteristicSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--characteristics",
        operation_description="Get the characteristics",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            ),
            openapi.Parameter(
                name="entity_id",
                default=1,
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                required=True,
                description="The id of the characteristic",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Characteristics",
                schema=CharacteristicSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request, entity_id):
        characteristics = Characteristic.objects.filter(entity_id=entity_id)
        serializer = CharacteristicSerializer(characteristics, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the egg group routes
class EggGroupRouteView(APIView):
    serializer_class = EggGroupRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--egg-group-routes",
        operation_description="Get the egg group routes",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            )
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Egg group routes",
                schema=EggGroupRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request):
        egg_group_routes = EggGroupRoute.objects.all()
        serializer = EggGroupRouteSerializer(egg_group_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the egg groups
class EggGroupsView(APIView):
    serializer_class = EggGroupSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--egg-groups",
        operation_description="Get the egg groups",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            ),
            openapi.Parameter(
                name="entity_id",
                default=1,
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                required=True,
                description="The id of the egg group",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Egg groups",
                schema=EggGroupSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request, entity_id):
        egg_groups = EggGroup.objects.filter(entity_id=entity_id)
        serializer = EggGroupSerializer(egg_groups, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the gender routes
class GenderRouteView(APIView):
    serializer_class = GenderRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--gender-routes",
        operation_description="Get the gender routes",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            )
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Gender routes",
                schema=GenderRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request):
        egg_group_routes = GenderRoute.objects.all()
        serializer = GenderRouteSerializer(egg_group_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the gender
class GenderView(APIView):
    serializer_class = GenderSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--genders",
        operation_description="Get the genders",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            ),
            openapi.Parameter(
                name="entity_id",
                default=1,
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                required=True,
                description="The id of the gender",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Genders",
                schema=GenderSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request, entity_id):
        genders = Gender.objects.filter(entity_id=entity_id)
        serializer = GenderSerializer(genders, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the growth rate routes
class GrowthRateRouteView(APIView):
    serializer_class = GrowthRateRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--growth-rate-routes",
        operation_description="Get the growth rate routes",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            )
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Growth rate routes",
                schema=GrowthRateRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request):
        growth_rate_routes = GrowthRateRoute.objects.all()
        serializer = GrowthRateRouteSerializer(growth_rate_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the growth rates
class GrowthRatesView(APIView):
    serializer_class = GrowthRateSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--growth-rates",
        operation_description="Get the growth rates",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            ),
            openapi.Parameter(
                name="entity_id",
                default=1,
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                required=True,
                description="The id of the growth rate",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Growth rates",
                schema=GrowthRateSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request, entity_id):
        growth_rates = GrowthRate.objects.filter(entity_id=entity_id)
        serializer = GrowthRateSerializer(growth_rates, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the nature routes
class NatureRouteView(APIView):
    serializer_class = NatureRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--nature-routes",
        operation_description="Get the nature routes",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            )
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Nature routes",
                schema=NatureRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request):
        nature_routes = NatureRoute.objects.all()
        serializer = NatureRouteSerializer(nature_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the natures
class NaturesView(APIView):
    serializer_class = NatureSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--natures",
        operation_description="Get the natures",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            ),
            openapi.Parameter(
                name="entity_id",
                default=1,
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                required=True,
                description="The id of the nature",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Natures",
                schema=NatureSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request, entity_id):
        natures = Nature.objects.filter(entity_id=entity_id)
        serializer = NatureSerializer(natures, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the pokeathlon stat routes
class PokeathlonStatRouteView(APIView):
    serializer_class = PokeathlonStatRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--pokeathlon-stat-routes",
        operation_description="Get the pokeathlon stat routes",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            )
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Pokeathlon stat routes",
                schema=PokeathlonStatRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request):
        pokeathlon_stat_routes = PokeathlonStatRoute.objects.all()
        serializer = PokeathlonStatRouteSerializer(pokeathlon_stat_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the pokeathlon stats
class PokeathlonStatsView(APIView):
    serializer_class = PokeathlonStatSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--pokeathlon-stats",
        operation_description="Get the pokeathlon stats",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            ),
            openapi.Parameter(
                name="entity_id",
                default=1,
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                required=True,
                description="The id of the pokeathlon stat",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Pokeathlon stats",
                schema=PokeathlonStatSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request, entity_id):
        pokeathlon_stats = PokeathlonStat.objects.filter(entity_id=entity_id)
        serializer = PokeathlonStatSerializer(pokeathlon_stats, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the pokemon routes
class PokemonRouteView(APIView):
    serializer_class = PokemonRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--pokemon-routes",
        operation_description="Get the pokemon routes",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            )
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Pokemon routes",
                schema=PokemonRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request):
        pokemon_routes = PokemonRoute.objects.all()
        serializer = PokemonRouteSerializer(pokemon_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the pokemon
class PokemonView(APIView):
    serializer_class = PokemonSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--pokemons",
        operation_description="Get the pokemons",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            ),
            openapi.Parameter(
                name="entity_id",
                default=1,
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                required=True,
                description="The id of the pokemon",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Pokemons",
                schema=PokemonSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request, entity_id):
        pokemons = Pokemon.objects.filter(entity_id=entity_id)
        serializer = PokemonSerializer(pokemons, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the pokemon color routes
class PokemonColorRouteView(APIView):
    serializer_class = PokemonColorRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--pokemon-color-routes",
        operation_description="Get the pokemon color routes",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            )
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Pokemon color routes",
                schema=PokemonColorRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request):
        pokemon_color_routes = PokemonColorRoute.objects.all()
        serializer = PokemonColorRouteSerializer(pokemon_color_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the pokemon colors
class PokemonColorsView(APIView):
    serializer_class = PokemonColorSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--pokemon-colors",
        operation_description="Get the pokemon colors",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            ),
            openapi.Parameter(
                name="entity_id",
                default=1,
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                required=True,
                description="The id of the pokemon color",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Pokemon colors",
                schema=PokemonColorSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request, entity_id):
        pokemon_colors = PokemonColor.objects.filter(entity_id=entity_id)
        serializer = PokemonColorSerializer(pokemon_colors, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the pokemon form routes
class PokemonFormRouteView(APIView):
    serializer_class = PokemonFormRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--pokemon-form-routes",
        operation_description="Get the pokemon form routes",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            )
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Pokemon form routes",
                schema=PokemonFormRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request):
        pokemon_form_routes = PokemonFormRoute.objects.all()
        serializer = PokemonFormRouteSerializer(pokemon_form_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the pokemon forms
class PokemonFormsView(APIView):
    serializer_class = PokemonFormSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--pokemon-forms",
        operation_description="Get the pokemon forms",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            ),
            openapi.Parameter(
                name="entity_id",
                default=1,
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                required=True,
                description="The id of the pokemon form",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Pokemon forms",
                schema=PokemonFormSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request, entity_id):
        pokemon_forms = PokemonForm.objects.filter(entity_id=entity_id)
        serializer = PokemonFormSerializer(pokemon_forms, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the pokemon habitat routes
class PokemonHabitatRouteView(APIView):
    serializer_class = PokemonHabitatRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--pokemon-habitat-routes",
        operation_description="Get the pokemon habitat routes",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            )
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Pokemon habitat routes",
                schema=PokemonHabitatRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request):
        pokemon_habitat_routes = PokemonHabitatRoute.objects.all()
        serializer = PokemonHabitatRouteSerializer(pokemon_habitat_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the pokemon habitats
class PokemonHabitatsView(APIView):
    serializer_class = PokemonHabitatSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--pokemon-habitats",
        operation_description="Get the pokemon habitats",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            ),
            openapi.Parameter(
                name="entity_id",
                default=1,
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                required=True,
                description="The id of the pokemon habitat",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Pokemon habitats",
                schema=PokemonHabitatSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request, entity_id):
        pokemon_habitats = PokemonHabitat.objects.filter(entity_id=entity_id)
        serializer = PokemonHabitatSerializer(pokemon_habitats, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the pokemon shape routes
class PokemonShapeRouteView(APIView):
    serializer_class = PokemonShapeRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--pokemon-shape-routes",
        operation_description="Get the pokemon shape routes",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            )
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Pokemon shape routes",
                schema=PokemonShapeRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request):
        pokemon_shape_routes = PokemonShapeRoute.objects.all()
        serializer = PokemonShapeRouteSerializer(pokemon_shape_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the pokemon shapes
class PokemonShapesView(APIView):
    serializer_class = PokemonShapeSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--pokemon-shapes",
        operation_description="Get the pokemon shapes",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            ),
            openapi.Parameter(
                name="entity_id",
                default=1,
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                required=True,
                description="The id of the pokemon shape",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Pokemon shapes",
                schema=PokemonShapeSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request, entity_id):
        pokemon_shapes = PokemonShape.objects.filter(entity_id=entity_id)
        serializer = PokemonShapeSerializer(pokemon_shapes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the pokemon species routes
class PokemonSpeciesRouteView(APIView):
    serializer_class = PokemonSpeciesRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--pokemon-species-routes",
        operation_description="Get the pokemon species routes",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            )
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Pokemon species routes",
                schema=PokemonSpeciesRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request):
        pokemon_species_routes = PokemonSpeciesRoute.objects.all()
        serializer = PokemonSpeciesRouteSerializer(pokemon_species_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the pokemon species
class PokemonSpeciesView(APIView):
    serializer_class = PokemonSpeciesSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--pokemon-species",
        operation_description="Get the pokemon species",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            ),
            openapi.Parameter(
                name="entity_id",
                default=1,
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                required=True,
                description="The id of the pokemon species",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Pokemon species",
                schema=PokemonSpeciesSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request, entity_id):
        pokemon_species = PokemonSpecies.objects.filter(entity_id=entity_id)
        serializer = PokemonSpeciesSerializer(pokemon_species, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the stat routes
class StatRouteView(APIView):
    serializer_class = StatRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--stat-routes",
        operation_description="Get the stat routes",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            )
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Stat routes",
                schema=StatRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request):
        stat_routes = StatRoute.objects.all()
        serializer = StatRouteSerializer(stat_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the stats
class StatsView(APIView):
    serializer_class = StatSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--stats",
        operation_description="Get the stats",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            ),
            openapi.Parameter(
                name="entity_id",
                default=1,
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                required=True,
                description="The id of the stat",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Stats",
                schema=StatSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request, entity_id):
        stats = Stat.objects.filter(entity_id=entity_id)
        serializer = StatSerializer(stats, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the type routes
class TypeRouteView(APIView):
    serializer_class = TypeRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--type-routes",
        operation_description="Get the type routes",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            )
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Type routes",
                schema=TypeRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request):
        type_routes = TypeRoute.objects.all()
        serializer = TypeRouteSerializer(type_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the types
class TypesView(APIView):
    serializer_class = TypeSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--types",
        operation_description="Get the types",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                default="",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="The token to authenticate the user",
            ),
            openapi.Parameter(
                name="entity_id",
                default=1,
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                required=True,
                description="The id of the type",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Types",
                schema=TypeSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Pokemon"],
    )
    def get(self, request, entity_id):
        types = Type.objects.filter(entity_id=entity_id)
        serializer = TypeSerializer(types, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
