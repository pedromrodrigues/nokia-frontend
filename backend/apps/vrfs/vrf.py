class Vrf():
    def __init__(self, name, vrf_type, admin_state, oper_state, oper_down_reason):
        self.name = name
        self.vrf_type = vrf_type
        self.admin_state = admin_state
        self.oper_state = oper_state
        self.oper_down_reason = oper_down_reason