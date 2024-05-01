# Imports
from apps.berries.models import (
    BerryRoute,
    Berry,
    BerryFirmnessRoute,
    BerryFirmness,
    BerryFlavorRoute,
    BerryFlavor,
)
from apps.berries.serializers import (
    BerryRouteSerializer,
    BerrySerializer,
    BerryFirmnessRouteSerializer,
    BerryFirmnessSerializer,
    BerryFlavorRouteSerializer,
    BerryFlavorSerializer,
)
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# View to serve the berries route
class BerryRouteView(APIView):
    serializer_class = BerryRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--berry-routes",
        operation_description="Get the berries routes",
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
                description="Berries routes",
                schema=BerryRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Berries"],
    )
    def get(self, request):
        berry_routes = BerryRoute.objects.all()
        serializer = BerryRouteSerializer(berry_routes, many=True)
        return Response(serializer.data)


# View to serve the berries
class BerriesView(APIView):
    serializer_class = BerrySerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--berries",
        operation_description="Get the berries",
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
                description="The id of the berry",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Berries",
                schema=BerrySerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Berries"],
    )
    def get(self, request, entity_id):
        berries = Berry.objects.filter(entity_id=entity_id)
        serializer = BerrySerializer(berries, many=True)
        return Response(serializer.data)


# View to serve the berry firmnesses route
class BerryFirmnessRouteView(APIView):
    serializer_class = BerryFirmnessRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--berry-firmness-routes",
        operation_description="Get the berry firmness routes",
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
                description="Berry firmness routes",
                schema=BerryFirmnessRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Berries"],
    )
    def get(self, request):
        berry_firmness_routes = BerryFirmnessRoute.objects.all()
        serializer = BerryFirmnessRouteSerializer(berry_firmness_routes, many=True)
        return Response(serializer.data)


# View to serve the berry firmnesses
class BerryFirmnessesView(APIView):
    serializer_class = BerryFirmnessSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--berry-firmnesses",
        operation_description="Get the berry firmnesses",
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
                description="The id of the berry firmness",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Berry firmnesses",
                schema=BerryFirmnessSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Berries"],
    )
    def get(self, request, entity_id):
        berry_firmnesses = BerryFirmness.objects.filter(entity_id=entity_id)
        serializer = BerryFirmnessSerializer(berry_firmnesses, many=True)
        return Response(serializer.data)


# View to server the berry flavor route
class BerryFlavorRouteView(APIView):
    serializer_class = BerryFlavorRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--berry-flavor-routes",
        operation_description="Get the berry flavor routes",
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
                description="Berry flavor routes",
                schema=BerryFlavorRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Berries"],
    )
    def get(self, request):
        berry_flavor_routes = BerryFlavorRoute.objects.all()
        serializer = BerryFlavorRouteSerializer(berry_flavor_routes, many=True)
        return Response(serializer.data)


# View to serve the berry flavors
class BerryFlavorsView(APIView):
    serializer_class = BerryFlavorSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--berry-flavors",
        operation_description="Get the berry flavors",
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
                description="The id of the berry flavor",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Berry flavors",
                schema=BerryFlavorSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Berries"],
    )
    def get(self, request, entity_id):
        berry_flavors = BerryFlavor.objects.filter(entity_id=entity_id)
        serializer = BerryFlavorSerializer(berry_flavors, many=True)
        return Response(serializer.data)
