# Imports
from apps.evolutions.models import (
    EvolutionChainRoute,
    EvolutionChain,
    EvolutionTriggerRoute,
    EvolutionTrigger,
)
from apps.evolutions.serializers import (
    EvolutionChainRouteSerializer,
    EvolutionChainSerializer,
    EvolutionTriggerRouteSerializer,
    EvolutionTriggerSerializer,
)
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# View to serve the evolution chain routes
class EvolutionChainRouteView(APIView):
    serializer_class = EvolutionChainRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--evolution-chain-routes",
        operation_description="Get the evolution chain routes",
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
                description="Evolution chain routes",
                schema=EvolutionChainRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Evolutions"],
    )
    def get(self, request):
        evolution_chain_routes = EvolutionChainRoute.objects.all()
        serializer = EvolutionChainRouteSerializer(evolution_chain_routes, many=True)
        return Response(serializer.data)


# View to serve the evolution chains
class EvolutionChainView(APIView):
    serializer_class = EvolutionChainSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--evolution-chains",
        operation_description="Get the evolution chains",
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
                description="The id of the evolution chain",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Evolution chains",
                schema=EvolutionChainSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Evolutions"],
    )
    def get(self, request, entity_id):
        evolution_chains = EvolutionChain.objects.filter(entity_id=entity_id)
        serializer = EvolutionChainSerializer(evolution_chains, many=True)
        return Response(serializer.data)


# View to serve the evolution trigger routes
class EvolutionTriggerRouteView(APIView):
    serializer_class = EvolutionTriggerRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--evolution-trigger-routes",
        operation_description="Get the evolution trigger routes",
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
                description="Evolution trigger routes",
                schema=EvolutionTriggerRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Evolutions"],
    )
    def get(self, request):
        evolution_trigger_routes = EvolutionTriggerRoute.objects.all()
        serializer = EvolutionTriggerRouteSerializer(
            evolution_trigger_routes, many=True
        )
        return Response(serializer.data)


# View to serve the evolution triggers
class EvolutionTriggerView(APIView):
    serializer_class = EvolutionTriggerSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--evolution-triggers",
        operation_description="Get the evolution triggers",
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
                description="The id of the evolution trigger",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Evolution triggers",
                schema=EvolutionTriggerSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Evolutions"],
    )
    def get(self, request, entity_id):
        evolution_triggers = EvolutionTrigger.objects.filter(entity_id=entity_id)
        serializer = EvolutionTriggerSerializer(evolution_triggers, many=True)
        return Response(serializer.data)
