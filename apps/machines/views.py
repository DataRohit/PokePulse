# Imports
from apps.machines.models import MachineRoute, Machine
from apps.machines.serializers import MachineRouteSerializer, MachineSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# View to serve the machine routes
class MachineRouteView(APIView):
    serializer_class = MachineRouteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--machine-routes",
        operation_description="Get the machine routes",
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
                description="Machine routes",
                schema=MachineRouteSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Machines"],
    )
    def get(self, request):
        machine_routes = MachineRoute.objects.all()
        serializer = MachineRouteSerializer(machine_routes, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# View to serve the machines
class MachinesView(APIView):
    serializer_class = MachineSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="api--machines",
        operation_description="Get the machines",
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
                description="The id of the machine",
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Machines",
                schema=MachineSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_401_UNAUTHORIZED: "Unauthorized",
        },
        tags=["Machines"],
    )
    def get(self, request, entity_id):
        machines = Machine.objects(entity_id=entity_id)
        serializer = MachineSerializer(machines, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
