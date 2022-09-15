from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContainerSerializer
import docker
import json
from json import JSONEncoder
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

class Container:
    def __init__(self, container_id, name, ip_address, ip6_address, image, state):
        self.container_id = container_id
        self.name = name
        self.ip_address = ip_address
        self.ip6_address = ip6_address
        self.image = image
        self.state = state

class Encoder(JSONEncoder):
    def default(self, j):
        return j.__dict__


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

        #container_json = json.dumps(container, indent=4, cls=Encoder)

        containers_list.append(container)

    serializer = ContainerSerializer(containers_list, many=True)

    containers_json = JSONRenderer().render(serializer.data)

    return HttpResponse(containers_json)



