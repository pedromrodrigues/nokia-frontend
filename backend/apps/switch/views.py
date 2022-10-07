from django.shortcuts import render
from .serializers import SwitchSerializer
from .models import Switch
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.core import serializers
from django.core.exceptions import PermissionDenied
import json



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def get_switches(request):

    serializer_class = SwitchSerializer
    queryset = Switch.objects.all()

    switches = queryset.filter(created_by=request.user)

    switches_s = serializer_class(switches, many=True)
    switches_j = JSONRenderer().render(switches_s.data)

    return HttpResponse(switches_j)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_switch(request):

    data = JSONParser().parse(request)
    serializer = SwitchSerializer(data=data)

    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return JsonResponse(serializer.data, status=201)
    
    return JsonResponse(serializer.errors, status=400)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_switch(request, switch_hostname):

    queryset = Switch.objects.all()
    edited_switch = queryset.get(hostname=switch_hostname)

    if (edited_switch):

        if request.user != edited_switch.created_by:
            raise PermissionDenied('Wrong object owner')
        
        data = JSONParser().parse(request)
        serializer = SwitchSerializer(edited_switch, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=204)
       
    return JsonResponse(serializer.errors, status=400)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_switch(request, switch_hostname):

    queryset = Switch.objects.all()
    delete_switch = queryset.get(hostname=switch_hostname)

    if (delete_switch):

        if request.user != delete_switch.created_by:
            raise PermissionDenied('Wrong object owner')
        
        delete_switch.delete()
        return HttpResponse(status=204)
    
    return HttpResponse(status=400)