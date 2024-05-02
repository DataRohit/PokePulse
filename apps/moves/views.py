# Imports
from apps.moves.models import (
    MoveRoute,
    Move,
    MoveAilmentRoute,
    MoveAilment,
    MoveCategoryRoute,
    MoveCategory,
    MoveDamageClassRoute,
    MoveDamageClass,
    MoveLearnMethodRoute,
    MoveLearnMethod,
    MoveTargetRoute,
    MoveTarget,
)
from apps.moves.serializers import (
    MoveRouteSerializer,
    MoveSerializer,
    MoveAilmentRouteSerializer,
    MoveAilmentSerializer,
    MoveCategoryRouteSerializer,
    MoveCategorySerializer,
    MoveDamageClassRouteSerializer,
    MoveDamageClassSerializer,
    MoveLearnMethodRouteSerializer,
    MoveLearnMethodSerializer,
    MoveTargetRouteSerializer,
    MoveTargetSerializer,
)
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# View to serve the MoveRoute model
class MoveRouteView(APIView):
    serializer_class = MoveRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--move-routes",
        operation_description="Get the move routes",
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
                description="Move routes",
                schema=MoveRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Moves"],
    )
    def get(self, request):
        move_routes = MoveRoute.objects.all()
        serializer = MoveRouteSerializer(move_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the Move model
class MovesView(APIView):
    serializer_class = MoveSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--moves",
        operation_description="Get the moves",
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
                description="The id of the move",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Moves",
                schema=MoveSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Moves"],
    )
    def get(self, request, entity_id):
        moves = Move.objects.filter(entity_id=entity_id)
        serializer = MoveSerializer(moves, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the MoveAilmentRoute model
class MoveAilmentRouteView(APIView):
    serializer_class = MoveAilmentRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--move-ailment-routes",
        operation_description="Get the move ailment routes",
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
                description="Move ailment routes",
                schema=MoveAilmentRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Moves"],
    )
    def get(self, request):
        move_ailment_routes = MoveAilmentRoute.objects.all()
        serializer = MoveAilmentRouteSerializer(move_ailment_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the MoveAilment model
class MoveAilmentsView(APIView):
    serializer_class = MoveAilmentSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--move-ailments",
        operation_description="Get the move ailments",
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
                description="The id of the move ailment",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Move ailments",
                schema=MoveAilmentSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Moves"],
    )
    def get(self, request, entity_id):
        move_ailments = MoveAilment.objects.filter(entity_id=entity_id)
        serializer = MoveAilmentSerializer(move_ailments, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the MoveCategoryRoute model
class MoveCategoryRouteView(APIView):
    serializer_class = MoveCategoryRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--move-category-routes",
        operation_description="Get the move category routes",
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
                description="Move category routes",
                schema=MoveCategoryRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Moves"],
    )
    def get(self, request):
        move_category_routes = MoveCategoryRoute.objects.all()
        serializer = MoveCategoryRouteSerializer(move_category_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the MoveCategory model
class MoveCategoriesView(APIView):
    serializer_class = MoveCategorySerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--move-categories",
        operation_description="Get the move categories",
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
                description="The id of the move category",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Move categories",
                schema=MoveCategorySerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Moves"],
    )
    def get(self, request, entity_id):
        move_categories = MoveCategory.objects.filter(entity_id=entity_id)
        serializer = MoveCategorySerializer(move_categories, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the MoveDamageClassRoute model
class MoveDamageClassRouteView(APIView):
    serializer_class = MoveDamageClassRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--move-damage-class-routes",
        operation_description="Get the move damage class routes",
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
                description="Move damage class routes",
                schema=MoveDamageClassRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Moves"],
    )
    def get(self, request):
        move_damage_class_routes = MoveDamageClassRoute.objects.all()
        serializer = MoveDamageClassRouteSerializer(move_damage_class_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the MoveDamageClass model
class MoveDamageClassesView(APIView):
    serializer_class = MoveDamageClassSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--move-damage-classes",
        operation_description="Get the move damage classes",
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
                description="The id of the move damage class",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Move damage classes",
                schema=MoveDamageClassSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Moves"],
    )
    def get(self, request, entity_id):
        move_damage_classes = MoveDamageClass.objects.filter(entity_id=entity_id)
        serializer = MoveDamageClassSerializer(move_damage_classes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the MoveLearnMethodRoute model
class MoveLearnMethodRouteView(APIView):
    serializer_class = MoveLearnMethodRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--move-learn-method-routes",
        operation_description="Get the move learn method routes",
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
                description="Move learn method routes",
                schema=MoveLearnMethodRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Moves"],
    )
    def get(self, request):
        move_learn_method_routes = MoveLearnMethodRoute.objects.all()
        serializer = MoveLearnMethodRouteSerializer(move_learn_method_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the MoveLearnMethod model
class MoveLearnMethodsView(APIView):
    serializer_class = MoveLearnMethodSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--move-learn-methods",
        operation_description="Get the move learn methods",
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
                description="The id of the move learn method",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Move learn methods",
                schema=MoveLearnMethodSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Moves"],
    )
    def get(self, request, entity_id):
        move_learn_methods = MoveLearnMethod.objects.filter(entity_id=entity_id)
        serializer = MoveLearnMethodSerializer(move_learn_methods, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the MoveTargetRoute model
class MoveTargetRouteView(APIView):
    serializer_class = MoveTargetRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--move-target-routes",
        operation_description="Get the move target routes",
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
                description="Move target routes",
                schema=MoveTargetRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Moves"],
    )
    def get(self, request):
        move_target_routes = MoveTargetRoute.objects.all()
        serializer = MoveTargetRouteSerializer(move_target_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the MoveTarget model
class MoveTargetsView(APIView):
    serializer_class = MoveTargetSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--move-targets",
        operation_description="Get the move targets",
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
                description="The id of the move target",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Move targets",
                schema=MoveTargetSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Moves"],
    )
    def get(self, request, entity_id):
        move_targets = MoveTarget.objects.filter(entity_id=entity_id)
        serializer = MoveTargetSerializer(move_targets, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
