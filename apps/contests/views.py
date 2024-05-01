# Imports
from apps.contests.models import (
    ContestTypeRoute,
    ContestType,
    ContestEffectRoute,
    ContestEffect,
    SuperContestEffectRoute,
    SuperContestEffect,
)
from apps.contests.serializers import (
    ContestTypeRouteSerializer,
    ContestTypeSerializer,
    ContestEffectRouteSerializer,
    ContestEffectSerializer,
    SuperContestEffectRouteSerializer,
    SuperContestEffectSerializer,
)
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# View to serve the contest type routes
class ContestTypeRouteView(APIView):
    serializer_class = ContestTypeRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--contest-type-routes",
        operation_description="Get the contest type routes",
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
                description="Contest type routes",
                schema=ContestTypeRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Contests"],
    )
    def get(self, request):
        contest_type_routes = ContestTypeRoute.objects.all()
        serializer = ContestTypeRouteSerializer(contest_type_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the contest types
class ContestTypesView(APIView):
    serializer_class = ContestTypeSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--contest-types",
        operation_description="Get the contest types",
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
                description="The id of the contest type",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Contest types",
                schema=ContestTypeSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Contests"],
    )
    def get(self, request, entity_id):
        contest_types = ContestType.objects.filter(entity_id=entity_id)
        serializer = ContestTypeSerializer(contest_types, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the contest effect routes
class ContestEffectRouteView(APIView):
    serializer_class = ContestEffectRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--contest-effect-routes",
        operation_description="Get the contest effect routes",
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
                description="Contest effect routes",
                schema=ContestEffectRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Contests"],
    )
    def get(self, request):
        contest_effect_routes = ContestEffectRoute.objects.all()
        serializer = ContestEffectRouteSerializer(contest_effect_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the contest effects
class ContestEffectsView(APIView):
    serializer_class = ContestEffectSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--contest-effects",
        operation_description="Get the contest effects",
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
                description="The id of the contest effect",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Contest effects",
                schema=ContestEffectSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Contests"],
    )
    def get(self, request, entity_id):
        contest_effects = ContestEffect.objects.filter(entity_id=entity_id)
        serializer = ContestEffectSerializer(contest_effects, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the super contest effect routes
class SuperContestEffectRouteView(APIView):
    serializer_class = SuperContestEffectRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--super-contest-effect-routes",
        operation_description="Get the super contest effect routes",
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
                description="Super contest effect routes",
                schema=SuperContestEffectRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Contests"],
    )
    def get(self, request):
        super_contest_effect_routes = SuperContestEffectRoute.objects.all()
        serializer = SuperContestEffectRouteSerializer(
            super_contest_effect_routes, many=True
        )
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the super contest effects
class SuperContestEffectsView(APIView):
    serializer_class = SuperContestEffectSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--super-contest-effects",
        operation_description="Get the super contest effects",
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
                description="The id of the super contest effect",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Super contest effects",
                schema=SuperContestEffectSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Contests"],
    )
    def get(self, request, entity_id):
        super_contest_effects = SuperContestEffect.objects.filter(entity_id=entity_id)
        serializer = SuperContestEffectSerializer(super_contest_effects, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
