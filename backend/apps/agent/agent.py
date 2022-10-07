class AgentState():
    def __init__(self, ip_fqdn, last_update, tests_performed, success_tests, unsuccess_tests, status_up, rtt_min, rtt_max, rtt_avg, rtt_std, admin_state):
        self.ip_fqdn = ip_fqdn
        self.last_update = last_update
        self.tests_performed = tests_performed
        self.success_tests = success_tests
        self.unsuccess_tests = unsuccess_tests
        self.status_up = status_up
        self.rtt_min = rtt_min
        self.rtt_max = rtt_max
        self.rtt_avg = rtt_avg
        self.rtt_std = rtt_std
        self.admin_state = admin_state

class AgentConfig():
    def __init__(self, ip_fqdn, admin_state, netinst, test_tool, source_ip, port, number_tests, number_packets, interval_period):
        self.ip_fqdn = ip_fqdn
        self.admin_state = admin_state
        self.netinst = netinst
        self.test_tool = test_tool
        self.source_ip = source_ip
        self.port = port
        self.number_tests = number_tests
        self.number_packets = number_packets
        self.interval_period = interval_period