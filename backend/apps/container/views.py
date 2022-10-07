from django.shortcuts import render
from .serializers import ContainerSerializer
from .container import Container
import docker
import json
from json import JSONEncoder
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_containers(request):

    containers_list = []
    socket_url = 'unix://var/run/docker.sock'
    client = docker.DockerClient(base_url=socket_url)

    for c in client.containers.list():
        container = Container(
            c.short_id,
            c.name,
            c.attrs['NetworkSettings']['Networks']['clab']['IPAddress'],
            c.attrs['NetworkSettings']['Networks']['clab']['GlobalIPv6Address'],
            c.attrs['Config']['Image'],
            c.status
        )
        containers_list.append(container)

    serializer = ContainerSerializer(containers_list, many=True)
    containers_json = JSONRenderer().render(serializer.data)

    return HttpResponse(containers_json)



