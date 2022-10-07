export default class Vrf {
    name!: string;
    vrf_type!: string;
    admin_state!: string;
    oper_state!: string;
    oper_down_reason!: string;

    constructor(jsonObj?: Vrf) {
        if (jsonObj) {
            this.name = jsonObj.name;
            this.vrf_type = jsonObj.vrf_type;
            this.admin_state = jsonObj.admin_state;
            this.oper_state = jsonObj.oper_state;
            this.oper_down_reason = jsonObj.oper_down_reason;
        }
    }
}