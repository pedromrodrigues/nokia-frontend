def list_all_interfaces():

    payload = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "get",
        "params": {
            "commands": [
                {
                "path": "/interface[name=*]",
                "datastore": "state",
                "recursive": False                
                }
            ]
        }
    }

    return payload

def iface_config(iface_name):

    payload = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "get",
        "params": {
            "commands": [
                {
                "path": f"/interface[name={iface_name}]",
                "datastore": "running",
                "recursive": True                }
            ]
        }
    }

    return payload