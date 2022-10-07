class Container:
    def __init__(self, container_id, name, ip_address, ip6_address, image, state):
        self.container_id = container_id
        self.name = name
        self.ip_address = ip_address
        self.ip6_address = ip6_address
        self.image = image
        self.state = state