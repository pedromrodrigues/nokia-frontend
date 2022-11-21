from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .payloads import agent_config_payload, agent_state_payload, agent_running_payload, agent_admin_state_payload, delete_agent_test_payload, set_agent_admin_state_payload, set_agent_test_admin_state_payload, delete_agent_test_payload
from .serializers import AgentStateSerializer
from .agent import AgentState, AgentConfig
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from apps.switch.models import Switch
import requests


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_agent_admin_state(request, hostname):

    queryset = Switch.objects.all()
    sr_switch = queryset.get(hostname=hostname)

    if (sr_switch):
        port = sr_switch.port

        url = f"https://{hostname}:{port}/jsonrpc"
        cert = '/home/pedro/Documents/ist-evpn/clab-evpn/ca/root/root-ca.pem'
        payload = agent_admin_state_payload()

        try:
            response = requests.post(url, auth=(
                'admin', 'admin'), json=payload, verify=cert)
        except:
            return HttpResponse(content=b'Unable to connect to the Switch', status=500)

        r_json = response.json()
        print(r_json)
        r_render = r_json['result'][0]

        return HttpResponse(r_render)

    return HttpResponse(status=404)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def set_agent_admin_state(request, hostname):

    queryset = Switch.objects.all()
    sr_switch = queryset.get(hostname=hostname)

    print(request.data)

    if (sr_switch):
        port = sr_switch.port

        url = f"https://{hostname}:{port}/jsonrpc"
        cert = '/home/pedro/Documents/ist-evpn/clab-evpn/ca/root/root-ca.pem'
        payload = set_agent_admin_state_payload(request.data)

        try:
            response = requests.post(url, auth=(
                'admin', 'admin'), json=payload, verify=cert)
        except:
            return HttpResponse(content=b'Unable to connect to the Switch', status=500)

        return HttpResponse(response)

    return HttpResponse(status=404)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_agent_state(request, hostname):

    queryset = Switch.objects.all()
    sr_switch = queryset.get(hostname=hostname)

    if (sr_switch):
        port = sr_switch.port
        targets = []

        url = f"https://{hostname}:{port}/jsonrpc"
        cert = '/home/pedro/Documents/ist-evpn/clab-evpn/ca/root/root-ca.pem'
        payload = agent_state_payload()

        try:
            response = requests.post(url, auth=(
                'admin', 'admin'), json=payload, verify=cert)
        except:
            return HttpResponse(content=b'Unable to connect to the Switch', status=500)

        if (response.status_code == 200):

            r_json = response.json()

            if ('state' in r_json['result'][0]):
                for peer in r_json['result'][0]['state']:
                    for target in r_json['result'][1]['targets']:
                        if (target['IP-FQDN'] == peer['IP'].split('-')[0]):
                            target_state = AgentState(
                                target['IP-FQDN'],
                                peer['last-update'],
                                peer['tests-performed'],
                                peer['successful-tests'],
                                peer['unsuccessful-tests'],
                                peer['status-up'],
                                peer['rtt-min-ms'],
                                peer['rtt-max-ms'],
                                peer['rtt-avg-ms'],
                                peer['rtt-stddev'],
                                target['admin-state']
                            )
                            targets.append(target_state)

        serializer = AgentStateSerializer(targets, many=True)
        targets_json = JSONRenderer().render(serializer.data)

        return HttpResponse(targets_json)

    return HttpResponse(status=404)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_agent_config(request, hostname):

    queryset = Switch.objects.all()
    sr_switch = queryset.get(hostname=hostname)

    if (sr_switch):
        port = sr_switch.port
        targets_config = []

        url = f"https://{hostname}:{port}/jsonrpc"
        cert = '/home/pedro/Documents/ist-evpn/clab-evpn/ca/root/root-ca.pem'
        payload = agent_config_payload()

        try:
            response = requests.post(url, auth=(
                'admin', 'admin'), json=payload, verify=cert)
        except:
            return HttpResponse(content=b'Unable to connect to the Switch', status=500)

        if (response.status_code == 200):

            r_json = response.json()
            if ('targets' in r_json['result'][0]):
                for target in r_json['result'][0]['targets']:
                    targets_config.append(target)

            targets_json = JSONRenderer().render(targets_config)

        return HttpResponse(targets_json)

    return HttpResponse(status=404)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def set_agent_running(request, hostname):

    queryset = Switch.objects.all()
    sr_switch = queryset.get(hostname=hostname)

    if (sr_switch):
        port = sr_switch.port

        url = f"https://{hostname}:{port}/jsonrpc"
        cert = '/home/pedro/Documents/ist-evpn/clab-evpn/ca/root/root-ca.pem'
        payload = agent_running_payload(request.data)

        try:
            response = requests.post(url, auth=(
                'admin', 'admin'), json=payload, verify=cert)
        except:
            return HttpResponse(content=b'Unable to connect to the Switch', status=500)

        return HttpResponse(response)

    return HttpResponse(status=404)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def set_agent_test_admin_state(request, hostname):

    queryset = Switch.objects.all()
    sr_switch = queryset.get(hostname=hostname)

    if (sr_switch):
        port = sr_switch.port

        url = f"https://{hostname}:{port}/jsonrpc"
        cert = '/home/pedro/Documents/ist-evpn/clab-evpn/ca/root/root-ca.pem'
        payload = set_agent_test_admin_state_payload(request.data)

        try:
            response = requests.post(url, auth=(
                'admin', 'admin'), json=payload, verify=cert)
        except:
            return HttpResponse(content=b'Unable to connect to the Switch', status=500)

        return HttpResponse(response)

    return HttpResponse(status=404)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_agent_test(request, hostname):

    queryset = Switch.objects.all()
    sr_switch = queryset.get(hostname=hostname)

    print("*************** ", hostname)

    if (sr_switch):
        port = sr_switch.port

        url = f"https://{hostname}:{port}/jsonrpc"
        cert = '/home/pedro/Documents/ist-evpn/clab-evpn/ca/root/root-ca.pem'
        payload = delete_agent_test_payload(request.data)

        try:
            response = requests.post(url, auth=(
                'admin', 'admin'), json=payload, verify=cert)
        except:
            return HttpResponse(content=b'Unable to connect to the Switch', status=500)

        return HttpResponse(response)

    return HttpResponse(status=404)