from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .payloads import list_all_interfaces, iface_config
from .interface import Interface
from .serializers import InterfaceSerializer
from apps.switch.models import Switch
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
import requests


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_interfaces(request, hostname):

    queryset = Switch.objects.all()
    sr_switch = queryset.get(hostname=hostname)

    if (sr_switch):

        port = sr_switch.port
        interfaces_list = []

        url = f"https://{hostname}:{port}/jsonrpc"
        cert = '/home/pedro/Documents/ist-evpn/clab-evpn/ca/root/root-ca.pem'
        payload = list_all_interfaces()

        try:
            response = requests.post(url, auth=(
                'admin', 'admin'), json=payload, verify=cert)
        except:
            return HttpResponse(content=b'Unable to connect to the Switch', status=500)

        r_json = response.json()

        if ('srl_nokia-interfaces:interface' in r_json['result'][0]):
            for interface in r_json['result'][0]['srl_nokia-interfaces:interface']:
                if 'oper-down-reason' in interface.keys():
                    iface = Interface(
                        interface['name'],
                        interface['admin-state'],
                        interface['oper-state'],
                        interface['oper-down-reason']
                    )
                else:
                    iface = Interface(
                        interface['name'],
                        interface['admin-state'],
                        interface['oper-state'],
                        ' '
                    )
                interfaces_list.append(iface)

        serializer = InterfaceSerializer(interfaces_list, many=True)
        interfaces_json = JSONRenderer().render(serializer.data)

        return HttpResponse(interfaces_json)

    return HttpResponse(status=404)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_interface_config(request, hostname, iface_name):

    queryset = Switch.objects.all()
    sr_switch = queryset.get(hostname=hostname)

    if (sr_switch):
        port = sr_switch.port

        url = f"https://{hostname}:{port}/jsonrpc"
        cert = '/home/pedro/Documents/ist-evpn/clab-evpn/ca/root/root-ca.pem'
        payload = iface_config(iface_name)

        try:
            response = requests.post(url, auth=(
                'admin', 'admin'), json=payload, verify=cert)
        except:
            return HttpResponse(content=b'Unable to connect to the Switch', status=500)

        r_json = response.json()

        if (r_json['result'][0]):
            r_parsed = r_json['result'][0]
            iface_config_json = JSONRenderer().render(r_parsed)

            return HttpResponse(iface_config_json)

    return HttpResponse(status=404)
        
