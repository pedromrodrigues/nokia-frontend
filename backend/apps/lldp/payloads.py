def list_lldp_neighbors():

    payload = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "get",
        "params": {
            "commands": [
                {
                "path": "/system/lldp/interface[name=*]",
                "datastore": "state",
                "recursive": True                
                }
            ]
        }
    }

    return payload