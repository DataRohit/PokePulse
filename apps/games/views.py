# Imports
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
from apps.games.serializers import (
    GenerationRouteSerializer,
    GenerationSerializer,
    PokedexRouteSerializer,
    PokedexSerializer,
    VersionRouteSerializer,
    VersionSerializer,
    VersionGroupRouteSerializer,
    VersionGroupSerializer,
)
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# View to serve the generations route
class GenerationRouteView(APIView):
    serializer_class = GenerationRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--generation-routes",
        operation_description="Get the generations routes",
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
                description="Generations routes",
                schema=GenerationRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Games"],
    )
    def get(self, request):
        generation_routes = GenerationRoute.objects.all()
        serializer = GenerationRouteSerializer(generation_routes, many=True)
        return Response(serializer.data)


# View to serve the generations
class GenerationsView(APIView):
    serializer_class = GenerationSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--generations",
        operation_description="Get the generations",
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
                description="The id of the generation",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Generations",
                schema=GenerationSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Games"],
    )
    def get(self, request, entity_id):
        generations = Generation.objects.filter(entity_id=entity_id)
        serializer = GenerationSerializer(generations, many=True)
        return Response(serializer.data)


# View for the pokedexes route
class PokedexRouteView(APIView):
    serializer_class = PokedexRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--pokedex-routes",
        operation_description="Get the pokedexes routes",
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
                description="Pokedexes routes",
                schema=PokedexRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Games"],
    )
    def get(self, request):
        pokedex_routes = PokedexRoute.objects.all()
        serializer = PokedexRouteSerializer(pokedex_routes, many=True)
        return Response(serializer.data)


# View for the pokedexes
class PokedexesView(APIView):
    serializer_class = PokedexSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--pokedexes",
        operation_description="Get the pokedexes",
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
                description="The id of the pokedex",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Pokedexes",
                schema=PokedexSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Games"],
    )
    def get(self, request, entity_id):
        pokedexes = Pokedex.objects.filter(entity_id=entity_id)
        serializer = PokedexSerializer(pokedexes, many=True)
        return Response(serializer.data)


# View for the versions route
class VersionRouteView(APIView):
    serializer_class = VersionRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--version-routes",
        operation_description="Get the versions routes",
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
                description="Versions routes",
                schema=VersionRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Games"],
    )
    def get(self, request):
        version_routes = VersionRoute.objects.all()
        serializer = VersionRouteSerializer(version_routes, many=True)
        return Response(serializer.data)


# View for the versions
class VersionsView(APIView):
    serializer_class = VersionSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--versions",
        operation_description="Get the versions",
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
                description="The id of the version",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Versions",
                schema=VersionSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Games"],
    )
    def get(self, request, entity_id):
        versions = Version.objects.filter(entity_id=entity_id)
        serializer = VersionSerializer(versions, many=True)
        return Response(serializer.data)


# View for the version groups route
class VersionGroupRouteView(APIView):
    serializer_class = VersionGroupRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--version-group-routes",
        operation_description="Get the version groups routes",
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
                description="Version groups routes",
                schema=VersionGroupRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Games"],
    )
    def get(self, request):
        version_group_routes = VersionGroupRoute.objects.all()
        serializer = VersionGroupRouteSerializer(version_group_routes, many=True)
        return Response(serializer.data)


# View for the version groups
class VersionGroupsView(APIView):
    serializer_class = VersionGroupSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--version-groups",
        operation_description="Get the version groups",
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
                description="The id of the version group",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Version groups",
                schema=VersionGroupSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Games"],
    )
    def get(self, request, entity_id):
        version_groups = VersionGroup.objects.filter(entity_id=entity_id)
        serializer = VersionGroupSerializer(version_groups, many=True)
        return Response(serializer.data)
