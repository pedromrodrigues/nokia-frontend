export default class AgentConfig {
    'IP-FQDN'!: string;
    'admin-state': string | null = 'enable';
    'network-instance'!: string;
    'test-tool'!: string;
    'source-ip'!: string;
    'port': number | null = null;
    'number-of-tests'!: number;
    'number-of-packets': number | null = 1;
    'interval-period': number | null = 1;  

    constructor(jsonObj?: AgentConfig) {
        if (jsonObj) {
            this["IP-FQDN"] = jsonObj["IP-FQDN"];
            this["admin-state"] = jsonObj["admin-state"];
            this["network-instance"] = jsonObj["network-instance"];
            this["test-tool"] = jsonObj["test-tool"];
            this["source-ip"] = jsonObj["source-ip"];
            this["port"] = jsonObj["port"];
            this["number-of-tests"] = jsonObj["number-of-tests"];
            this["number-of-packets"] = jsonObj["number-of-packets"];
            this["interval-period"] = jsonObj["interval-period"];

            if (!jsonObj["admin-state"]) {
                this["admin-state"] = "disable";
            }

            if (!jsonObj["number-of-packets"]) {
                this["number-of-packets"] = 1;
            }

            if (!jsonObj["interval-period"]) {
                this["interval-period"] = 1;
            }
        }
    }
}