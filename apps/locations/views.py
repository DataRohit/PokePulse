# Imports
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
from apps.locations.serializers import (
    LocationRouteSerializer,
    LocationSerializer,
    LocationAreaRouteSerializer,
    LocationAreaSerializer,
    PalParkAreaRouteSerializer,
    PalParkAreaSerializer,
    RegionRouteSerializer,
    RegionSerializer,
)
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# View to serve the location routes
class LocationRouteView(APIView):
    serializer_class = LocationRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--location-routes",
        operation_description="Get the location routes",
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
                description="Location routes",
                schema=LocationRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Locations"],
    )
    def get(self, request):
        location_routes = LocationRoute.objects.all()
        serializer = LocationRouteSerializer(location_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the location
class LocationsView(APIView):
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--locations",
        operation_description="Get the locations",
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
                description="The id of the location",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Locations",
                schema=LocationSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Locations"],
    )
    def get(self, request, entity_id):
        locations = Location.objects.filter(entity_id=entity_id)
        serializer = LocationSerializer(locations, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the location area routes
class LocationAreaRouteView(APIView):
    serializer_class = LocationAreaRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--location-area-routes",
        operation_description="Get the location area routes",
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
                description="Location area routes",
                schema=LocationAreaRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Locations"],
    )
    def get(self, request):
        location_area_routes = LocationAreaRoute.objects.all()
        serializer = LocationAreaRouteSerializer(location_area_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the location areas
class LocationAreasView(APIView):
    serializer_class = LocationAreaSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--location-areas",
        operation_description="Get the location areas",
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
                description="The id of the location area",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Location areas",
                schema=LocationAreaSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Locations"],
    )
    def get(self, request, entity_id):
        location_areas = LocationArea.objects.filter(entity_id=entity_id)
        serializer = LocationAreaSerializer(location_areas, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the pal park area routes
class PalParkAreaRouteView(APIView):
    serializer_class = PalParkAreaRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--pal-park-area-routes",
        operation_description="Get the pal park area routes",
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
                description="Pal park area routes",
                schema=PalParkAreaRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Locations"],
    )
    def get(self, request):
        pal_park_area_routes = PalParkAreaRoute.objects.all()
        serializer = PalParkAreaRouteSerializer(pal_park_area_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the pal park areas
class PalParkAreasView(APIView):
    serializer_class = PalParkAreaSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--pal-park-areas",
        operation_description="Get the pal park areas",
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
                description="The id of the pal park area",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Pal park areas",
                schema=PalParkAreaSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Locations"],
    )
    def get(self, request, entity_id):
        pal_park_areas = PalParkArea.objects.filter(entity_id=entity_id)
        serializer = PalParkAreaSerializer(pal_park_areas, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the region routes
class RegionRouteView(APIView):
    serializer_class = RegionRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--region-routes",
        operation_description="Get the region routes",
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
                description="Region routes",
                schema=RegionRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Locations"],
    )
    def get(self, request):
        region_routes = RegionRoute.objects.all()
        serializer = RegionRouteSerializer(region_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the regions
class RegionsView(APIView):
    serializer_class = RegionSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--regions",
        operation_description="Get the regions",
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
                description="The id of the region",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Regions",
                schema=RegionSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Locations"],
    )
    def get(self, request, entity_id):
        regions = Region.objects.filter(entity_id=entity_id)
        serializer = RegionSerializer(regions, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
