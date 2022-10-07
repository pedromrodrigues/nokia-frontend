def list_vrfs():

    payload = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "get",
        "params": {
            "commands": [
                {
                "path": "/network-instance[name=*]",
                "datastore": "state",
                "recursive": False                }
            ]
        }
    }

    return payload

def vrf_config(name):

    payload = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "get",
        "params": {
            "commands": [
                {
                "path": f"/network-instance[name={name}]",
                "datastore": "running",
                "recursive": True                }
            ]
        }
    }

    return payload
