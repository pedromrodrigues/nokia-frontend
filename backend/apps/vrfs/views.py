from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.http import HttpResponse
import requests
from .payloads import list_vrfs, vrf_config
from .serializers import VrfSerializer
from .vrf import Vrf
from apps.switch.models import Switch


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_net_instances(request, hostname, vrf):

    queryset = Switch.objects.all()
    sr_switch = queryset.get(hostname=hostname)

    if (sr_switch):

        port = sr_switch.port
        network_instances = []

        url = f"https://{hostname}:{port}/jsonrpc"
        cert = '/home/pedro/Documents/ist-evpn/clab-evpn/ca/root/root-ca.pem'
        payload = list_vrfs()

        try:
            response = requests.post(url, auth=(
                'admin', 'admin'), json=payload, verify=cert)
        except:
            return HttpResponse(content=b'Unable to connect to the Switch', status=500)

        r_json = response.json()

        if ('srl_nokia-network-instance:network-instance' in r_json['result'][0]):
            for netinst in r_json['result'][0]['srl_nokia-network-instance:network-instance']:
                if 'oper-down-reason' in netinst.keys() and netinst['type'] == f'srl_nokia-network-instance:{vrf}':
                    n_inst = Vrf(
                        netinst['name'],
                        f'{vrf}',
                        netinst['admin-state'],
                        netinst['oper-state'],
                        netinst['oper-down-reason']
                    )
                    network_instances.append(n_inst)
                elif netinst['type'] == f'srl_nokia-network-instance:{vrf}':
                    n_inst = Vrf(
                        netinst['name'],
                        f'{vrf}',
                        netinst['admin-state'],
                        netinst['oper-state'],
                        ' '
                    )
                    network_instances.append(n_inst)

        serializer = VrfSerializer(network_instances, many=True)
        network_instances_json = JSONRenderer().render(serializer.data)

        return HttpResponse(network_instances_json)

    return HttpResponse(status=404)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_vrf_config(request, hostname, vrf_name):

    queryset = Switch.objects.all()
    sr_switch = queryset.get(hostname=hostname)

    if (sr_switch):

        port = sr_switch.port

        url = f"https://{hostname}:{port}/jsonrpc"
        cert = '/home/pedro/Documents/ist-evpn/clab-evpn/ca/root/root-ca.pem'
        payload = vrf_config(vrf_name)

        try:
            response = requests.post(url, auth=(
                'admin', 'admin'), json=payload, verify=cert)
        except:
            return HttpResponse(content=b'Unable to connect to the Switch', status=500)

        r_json = response.json()
        r_parsed = r_json['result'][0]
        r_rendered = JSONRenderer().render(r_parsed)

        return HttpResponse(r_rendered)

    return HttpResponse(status=404)