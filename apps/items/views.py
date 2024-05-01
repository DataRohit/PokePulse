# Imports
from apps.items.models import (
    ItemRoute,
    Item,
    ItemAttributeRoute,
    ItemAttribute,
    ItemCategoryRoute,
    ItemCategory,
    ItemFlingEffectRoute,
    ItemFlingEffect,
    ItemPocketRoute,
    ItemPocket,
)
from apps.items.serializers import (
    ItemRouteSerializer,
    ItemSerializer,
    ItemAttributeRouteSerializer,
    ItemAttributeSerializer,
    ItemCategoryRouteSerializer,
    ItemCategorySerializer,
    ItemFlingEffectRouteSerializer,
    ItemFlingEffectSerializer,
    ItemPocketRouteSerializer,
    ItemPocketSerializer,
)
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# View to serve the item routes
class ItemRouteView(APIView):
    serializer_class = ItemRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--item-routes",
        operation_description="Get the item routes",
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
                description="Item routes",
                schema=ItemRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Items"],
    )
    def get(self, request):
        item_routes = ItemRoute.objects.all()
        serializer = ItemRouteSerializer(item_routes, many=True)
        return Response(serializer.data)


# View to serve the items
class ItemsView(APIView):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--items",
        operation_description="Get the items",
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
                description="The id of the item",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Items",
                schema=ItemSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Items"],
    )
    def get(self, request, entity_id):
        items = Item.objects.filter(entity_id=entity_id)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


# View to serve the item attribute routes
class ItemAttributeRouteView(APIView):
    serializer_class = ItemAttributeRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--item-attribute-routes",
        operation_description="Get the item attribute routes",
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
                description="Item attribute routes",
                schema=ItemAttributeRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Items"],
    )
    def get(self, request):
        item_attribute_routes = ItemAttributeRoute.objects.all()
        serializer = ItemAttributeRouteSerializer(item_attribute_routes, many=True)
        return Response(serializer.data)


# View to serve the item attributes
class ItemAttributesView(APIView):
    serializer_class = ItemAttributeSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--item-attributes",
        operation_description="Get the item attributes",
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
                description="The id of the item attribute",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Item attributes",
                schema=ItemAttributeSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Items"],
    )
    def get(self, request, entity_id):
        item_attributes = ItemAttribute.objects.filter(entity_id=entity_id)
        serializer = ItemAttributeSerializer(item_attributes, many=True)
        return Response(serializer.data)


# View to serve the item category routes
class ItemCategoryRouteView(APIView):
    serializer_class = ItemCategoryRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--item-category-routes",
        operation_description="Get the item category routes",
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
                description="Item category routes",
                schema=ItemCategoryRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Items"],
    )
    def get(self, request):
        item_category_routes = ItemCategoryRoute.objects.all()
        serializer = ItemCategoryRouteSerializer(item_category_routes, many=True)
        return Response(serializer.data)


# View to serve the item categories
class ItemCategoriesView(APIView):
    serializer_class = ItemCategorySerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--item-categories",
        operation_description="Get the item categories",
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
                description="The id of the item category",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Item categories",
                schema=ItemCategorySerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Items"],
    )
    def get(self, request, entity_id):
        item_categories = ItemCategory.objects.filter(entity_id=entity_id)
        serializer = ItemCategorySerializer(item_categories, many=True)
        return Response(serializer.data)


# View to serve the item fling effect routes
class ItemFlingEffectRouteView(APIView):
    serializer_class = ItemFlingEffectRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--item-fling-effect-routes",
        operation_description="Get the item fling effect routes",
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
                description="Item fling effect routes",
                schema=ItemFlingEffectRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Items"],
    )
    def get(self, request):
        item_fling_effect_routes = ItemFlingEffectRoute.objects.all()
        serializer = ItemFlingEffectRouteSerializer(item_fling_effect_routes, many=True)
        return Response(serializer.data)


# View to serve the item fling effects
class ItemFlingEffectsView(APIView):
    serializer_class = ItemFlingEffectSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--item-fling-effects",
        operation_description="Get the item fling effects",
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
                description="The id of the item fling effect",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Item fling effects",
                schema=ItemFlingEffectSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Items"],
    )
    def get(self, request, entity_id):
        item_fling_effects = ItemFlingEffect.objects.filter(entity_id=entity_id)
        serializer = ItemFlingEffectSerializer(item_fling_effects, many=True)
        return Response(serializer.data)


# View to serve the item pocket routes
class ItemPocketRouteView(APIView):
    serializer_class = ItemPocketRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--item-pocket-routes",
        operation_description="Get the item pocket routes",
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
                description="Item pocket routes",
                schema=ItemPocketRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Items"],
    )
    def get(self, request):
        item_pocket_routes = ItemPocketRoute.objects.all()
        serializer = ItemPocketRouteSerializer(item_pocket_routes, many=True)
        return Response(serializer.data)


# View to serve the item pockets
class ItemPocketsView(APIView):
    serializer_class = ItemPocketSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--item-pockets",
        operation_description="Get the item pockets",
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
                description="The id of the item pocket",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Item pockets",
                schema=ItemPocketSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Items"],
    )
    def get(self, request, entity_id):
        item_pockets = ItemPocket.objects.filter(entity_id=entity_id)
        serializer = ItemPocketSerializer(item_pockets, many=True)
        return Response(serializer.data)
