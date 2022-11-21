def agent_admin_state_payload():

    payload = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "get",
        "params": {
            "commands": [
                {
                "path": "/overlay-test/admin-state",
                "datastore": "running",
                "recursive": False
                },
            ],
        }
    }

    return payload

def set_agent_admin_state_payload(data):

    payload = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "set",
        "params": {
            "commands": [
                {
                "action": "update",
                "path": f"/overlay-test/admin-state:{data['admin_state']}",
                },
            ],
        }
    }

    return payload


def agent_config_payload():

    payload = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "get",
        "params": {
            "commands": [
                {
                "path": "/overlay-test",
                "datastore": "running",
                "recursive": True
                },
            ],
        }
    }

    return payload


def agent_state_payload():

    payload = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "get",
        "params": {
            "commands": [
                {
                "path": "/overlay-test",
                "datastore": "state",
                "recursive": True
                },
                {
                "path": "/overlay-test",
                "datastore": "running",
                "recursive": True
                },
            ],
        }
    }

    return payload

def agent_running_payload(data):

    payload = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "set",
        "params": {
            "commands": [
                {
                "action": "update",
                "path": f"/overlay-test/targets[IP-FQDN={data['destinationIP']}]",
                "value": {
                    "admin-state": "enable",
                    "network-instance": f"{data['netinst']}",
                    "test-tool": f"{data['testTool']}",
                    "number-of-tests": f"{data['numberTests']}",
                    "source-ip": f"{data['sourceIP']}",
                    }
                }
            ]
        }
    }

    if (data['port']):
        payload['params']['commands'][0]['value'].update({'port': data['port']})
    if (data['numberPackets']):
        payload['params']['commands'][0]['value'].update({'number-of-packets': data['numberPackets']})
    if (data['time']):
        payload['params']['commands'][0]['value'].update({'interval-period': data['time']})

    return payload

def set_agent_test_admin_state_payload(data):

    payload = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "set",
        "params": {
            "commands": [
                {
                "action": "update",
                "path": f"/overlay-test/targets[IP-FQDN={data['destinationIP']}]",
                "value": {
                    "admin-state": f"{data['admin_state']}",
                }
                },
            ],
        }
    }

    return payload

def delete_agent_test_payload(data):

    payload = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "set",
        "params": {
            "commands": [
                {
                "action": "delete",
                "path": f"/overlay-test/targets[IP-FQDN={data['destinationIP']}]",
                },
            ],
        }
    }

    return payload