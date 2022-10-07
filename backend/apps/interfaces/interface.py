class Interface:
    def __init__(self, name, admin_state, oper_state, oper_down_reason):
        self.name = name
        self.admin_state = admin_state
        self.oper_state = oper_state
        self.oper_down_reason = oper_down_reason