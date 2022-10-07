from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes, renderer_classes
from rest_framework.renderers import JSONRenderer
from .serializers import MyUserSerializer
from rest_framework.response import Response


class MyUser:
    def __init__(self, username, is_staff, last_login, date_joined, name=None, email=None):
        self.username = username
        self.is_staff = is_staff
        self.name = name
        self.email = email
        self.last_login = last_login
        self.date_joined = date_joined

        
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def get_my_user(request):

    my_user = MyUser(
        request.user.username,
        request.user.is_staff,
        request.user.last_login,
        request.user.date_joined,
        request.user.get_full_name(),
        request.user.email
        )

    user_serializer = MyUserSerializer(my_user)

    return Response(user_serializer.data)