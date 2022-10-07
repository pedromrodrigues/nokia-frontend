from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http import HttpResponse
import requests
from .serializers import LldpSerializer
from .lldp import Lldp
from .payloads import list_lldp_neighbors

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_lldp_neighbors(request, container):

    lldp_neighbors = []
    url = f"https://{container}/jsonrpc"
    cert = '/home/pedro/Documents/evpn/clab-clos10/ca/root/root-ca.pem'
    payload = list_lldp_neighbors()

    response = requests.post(url, auth=('admin', 'admin'), json=payload, verify=cert)

    r_json = response.json()

    for interface in r_json['result'][0]['interface']:
        if 'neighbor' in interface.keys():
            for neighbor in interface['neighbor']:
                lldp_neighbor = Lldp(
                    interface['name'],
                    neighbor['id'],
                    neighbor['first-message'],
                    neighbor['last-update'],
                    neighbor['system-name'],
                    neighbor['port-id']
                )
                lldp_neighbors.append(lldp_neighbor)

    serializer = LldpSerializer(lldp_neighbors, many=True)
    lldp_neighbors_json = JSONRenderer().render(serializer.data)

    return HttpResponse(lldp_neighbors_json)
        