# Imports
from apps.encounters.models import (
    EncounterMethodRoute,
    EncounterMethod,
    EncounterConditionRoute,
    EncounterCondition,
    EncounterConditionValueRoute,
    EncounterConditionValue,
)
from apps.encounters.serializers import (
    EncounterMethodRouteSerializer,
    EncounterMethodSerializer,
    EncounterConditionRouteSerializer,
    EncounterConditionSerializer,
    EncounterConditionValueRouteSerializer,
    EncounterConditionValueSerializer,
)
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# View to serve the encounter method routes
class EncounterMethodRouteView(APIView):
    serializer_class = EncounterMethodRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--encounter-method-routes",
        operation_description="Get the encounter method routes",
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
                description="Encounter method routes",
                schema=EncounterMethodRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Encounters"],
    )
    def get(self, request):
        encounter_method_routes = EncounterMethodRoute.objects.all()
        serializer = EncounterMethodRouteSerializer(encounter_method_routes, many=True)
        return Response(serializer.data)


# View to serve the encounter methods
class EncounterMethodView(APIView):
    serializer_class = EncounterMethodSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--encounter-methods",
        operation_description="Get the encounter methods",
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
                description="The id of the encounter method",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Encounter methods",
                schema=EncounterMethodSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Encounters"],
    )
    def get(self, request, entity_id):
        encounter_methods = EncounterMethod.objects.filter(entity_id=entity_id)
        serializer = EncounterMethodSerializer(encounter_methods, many=True)
        return Response(serializer.data)


# View to serve the encounter condition routes
class EncounterConditionRouteView(APIView):
    serializer_class = EncounterConditionRoute
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--encounter-condition-routes",
        operation_description="Get the encounter condition routes",
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
                description="Encounter condition routes",
                schema=EncounterConditionRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Encounters"],
    )
    def get(self, request):
        encounter_condition_routes = EncounterConditionRoute.objects.all()
        serializer = EncounterConditionRouteSerializer(
            encounter_condition_routes, many=True
        )
        return Response(serializer.data)


# View to serve the encounter conditions
class EncounterConditionView(APIView):
    serializer_class = EncounterCondition
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--encounter-conditions",
        operation_description="Get the encounter conditions",
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
                description="The id of the encounter condition",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Encounter conditions",
                schema=EncounterConditionSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Encounters"],
    )
    def get(self, request, entity_id):
        encounter_conditions = EncounterCondition.objects.filter(entity_id=entity_id)
        serializer = EncounterConditionSerializer(encounter_conditions, many=True)
        return Response(serializer.data)


# View to serve the encounter condition value routes
class EncounterConditionValueRouteView(APIView):
    serializer_class = EncounterConditionValueRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--encounter-condition-value-routes",
        operation_description="Get the encounter condition value routes",
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
                description="Encounter condition value routes",
                schema=EncounterConditionValueRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Encounters"],
    )
    def get(self, request):
        encounter_condition_value_routes = EncounterConditionValueRoute.objects.all()
        serializer = EncounterConditionValueRouteSerializer(
            encounter_condition_value_routes, many=True
        )
        return Response(serializer.data)


# View to serve the encounter condition value
class EncounterConditionValueView(APIView):
    serializer_class = EncounterConditionValueSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--encounter-condition-values",
        operation_description="Get the encounter condition values",
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
                description="The id of the encounter condition value",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Encounter condition values",
                schema=EncounterConditionValueSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Encounters"],
    )
    def get(self, request, entity_id):
        encounter_condition_values = EncounterConditionValue.objects.filter(
            entity_id=entity_id
        )
        serializer = EncounterConditionValueSerializer(
            encounter_condition_values, many=True
        )
        return Response(serializer.data)
