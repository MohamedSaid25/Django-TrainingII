from rest_framework import generics, status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from knox.auth import AuthToken
from users.models import User
from .serializers import RegisterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from knox.auth import AuthToken, TokenAuthentication


class RegistrationView(generics.CreateAPIView):

    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):

        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        model_serializer = RegisterSerializer(data=serializer.data)
        model_serializer.is_valid(raise_exception=True)

        [username, email, password, bio] = [model_serializer.data['username'],
                                            model_serializer.data['email'], model_serializer.data['password'], model_serializer.data['bio']]

        user = User.objects.create_user(
            username=username, email=email, password=password, bio=bio)

        _, token = AuthToken.objects.create(user)

        return Response({
            "token": token,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "bio": user.bio
            }
        }, status=status.HTTP_201_CREATED)


class LoginView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = AuthTokenSerializer

    def create(self, request, *args, **kwargs):

        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        _, token = AuthToken.objects.create(user)

        return Response({
            "token": token,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "bio": user.bio
            }
        }, status=status.HTTP_200_OK)
