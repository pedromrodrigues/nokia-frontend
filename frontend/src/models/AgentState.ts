import { ISOtoString } from "@/services/ConvertDate";

export default class AgentState {
    ip_fqdn!: string;
    last_update!: string;
    tests_performed!: string;
    success_tests!: string;
    unsuccess_tests!: string;
    status_up!: boolean;
    rtt_min!: string;
    rtt_max!: string;
    rtt_avg!: string;
    rtt_std!: string;
    admin_state!: string;

    constructor(jsonObj?: AgentState) {
        if (jsonObj) {
            this.ip_fqdn = jsonObj.ip_fqdn;
            this.last_update = jsonObj.last_update;
            this.tests_performed = jsonObj.tests_performed;
            this.success_tests = jsonObj.success_tests;
            this.unsuccess_tests = jsonObj.unsuccess_tests;
            this.status_up = jsonObj.status_up;
            this.rtt_min = jsonObj.rtt_min;
            this.rtt_max = jsonObj.rtt_max;
            this.rtt_avg = jsonObj.rtt_avg;
            this.rtt_std = jsonObj.rtt_std;
            this.admin_state = jsonObj.admin_state;

            if (jsonObj.last_update) {
                this.last_update = ISOtoString(this.last_update);
            }
        }
    }
}