# Imports
from apps.utilities.models import LanguageRoute, Language
from apps.utilities.serializers import LanguageRouteSerializer, LanguageSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# View for LanguageRoute
class LanguageRouteView(APIView):
    serializer_class = LanguageRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--language-routes",
        operation_description="Get the language routes",
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
                description="Language routes",
                schema=LanguageRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Utilities"],
    )
    def get(self, request):
        language_routes = LanguageRoute.objects.all()
        serializer = LanguageRouteSerializer(language_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View for Language
class LanguagesView(APIView):
    serializer_class = LanguageSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--languages",
        operation_description="Get the languages",
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
                description="The id of the language",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Languages",
                schema=LanguageSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Utilities"],
    )
    def get(self, request, entity_id):
        languages = Language.objects.filter(entity_id=entity_id)
        serializer = LanguageSerializer(languages, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)