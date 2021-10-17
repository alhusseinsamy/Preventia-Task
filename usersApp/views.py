from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from usersApp import serializers


# Create your views here.

class TestView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        return Response(
            {
                "details": "Hello",
            },
            status=200
        )

class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': {
                'id': user.normaluser.id,
                'username': user.normaluser.username,
                'first_name': user.normaluser.first_name,
                'last_name': user.normaluser.last_name,
                'email': user.normaluser.email
            },
            'email': user.email
        })

class Logout(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=200)


class NormalUserView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    serializer_class = serializers.CreateUpdateUserSerializer

    def get_object(self):
        return self.request.user.normaluser

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = serializer.instance
        return Response(
            {
                "details": "User Created Successfully",
            },
            status=201
        )

    def put(self, request):
        instance = self.get_object()
        serializer = self.serializer_class(
            instance, data=request.data, partial=True
            )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "details": "User Updated Successfully",
            "data": serializer.data
        })

