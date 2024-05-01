# Imports
import os
from apps.core.serializers import CustomAuthTokenSerializer
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import View
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
import secrets
import smtplib


# Initialize the user model
User = get_user_model()


# Custom view to obtain an auth token
class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    @swagger_auto_schema(
        operation_id="api--obtain-auth-token",
        operation_description="Obtain an auth token for a user",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["email", "password"],
            properties={
                "email": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={
            status.HTTP_200_OK: openapi.Response(
                "The auth token",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={"token": openapi.Schema(type=openapi.TYPE_STRING)},
                ),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
        },
        tags=["Rest API Authentication"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomCreateUserView(APIView):
    # Set the permission class to allow any
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        operation_id="api--create-user",
        operation_description="Create a user",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["email", "password"],
            properties={
                "email": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={
            status.HTTP_201_CREATED: openapi.Response(
                "The user",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={"email": openapi.Schema(type=openapi.TYPE_STRING)},
                ),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request",
        },
        tags=["Rest API Authentication"],
    )
    def post(self, request, *args, **kwargs):
        # Extract email and password from request data
        email = request.data.get("email")
        password = request.data.get("password")

        # Validate email format
        try:
            validate_email(email)
        except ValidationError:
            return Response(
                {"error": "Invalid email format."}, status=status.HTTP_400_BAD_REQUEST
            )

        # Create user
        if email and password:
            try:
                # Generate a random token for the user
                token_key = secrets.token_urlsafe(
                    64
                )  # Generate a 64-character random token

                # Create the user with active status set to False and using the token key
                user = User.objects.create_user(
                    email=email, password=password, is_active=False, token_key=token_key
                )
                # Send verification email
                verification_link = reverse(
                    "api--verify-email", kwargs={"token_key": token_key}
                )
                verification_url = request.build_absolute_uri(verification_link)
                send_verification_email(email, verification_url)
                return Response({"email": user.email}, status=status.HTTP_201_CREATED)

            # If user with the email already exists
            except IntegrityError:
                return Response(
                    {"error": "User with this email already exists."},
                    status=status.HTTP_409_CONFLICT,
                )
        else:
            return Response(
                {"error": "Email and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )


# Function to send a verification email
def send_verification_email(email, verification_url):
    # Set the subject and message
    subject = "PokePulse - Verify Your Email Address"
    html_message = render_to_string(
        "email_verification.html", {"context": {"verification_url": verification_url}}
    )

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = os.environ.get("EMAIL_HOST_USER")
    message["To"] = email
    message["Subject"] = subject

    # Add HTML content to the email
    message.attach(MIMEText(html_message, "html"))

    # Connect to the SMTP server
    with smtplib.SMTP(
        host=os.environ.get("EMAIL_HOST"), port=os.environ.get("EMAIL_PORT")
    ) as server:
        # Start tls
        server.starttls()

        # Login
        server.login(
            os.environ.get("EMAIL_HOST_USER"), os.environ.get("EMAIL_HOST_PASSWORD")
        )

        # Send the email
        server.sendmail(os.environ.get("EMAIL_HOST_USER"), email, message.as_string())


# View to handle user email verification
class VerifyEmailView(View):
    def get(self, request, token_key):
        # Get the user object
        user = get_object_or_404(User, token_key=token_key)

        # Set the user status to active
        user.is_active = True

        # Remove the token key
        user.token_key = None

        # Save the user
        user.save()

        # Redirect
        return redirect(reverse("schema-swagger-ui"))
