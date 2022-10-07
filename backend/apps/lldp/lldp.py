class Lldp():
    def __init__(self, iface_name, neighbor_id, neighbor_first_message, neighbor_last_update, neighbor_name, neighbor_iface):
        self.iface_name = iface_name
        self.neighbor_id = neighbor_id
        self.neighbor_first_message = neighbor_first_message
        self.neighbor_last_update = neighbor_last_update
        self.neighbor_name = neighbor_name
        self.neighbor_iface = neighbor_iface