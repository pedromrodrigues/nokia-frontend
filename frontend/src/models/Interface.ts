export default class Interface {
    name!: string;
    admin_state!: string;
    oper_state!: string;
    oper_down_reason!: string;

    constructor(jsonObj?: Interface) {
        if (jsonObj) {
            this.name = jsonObj.name;
            this.admin_state = jsonObj.admin_state;
            this.oper_state = jsonObj.oper_state;
            this.oper_down_reason = jsonObj.oper_down_reason;
        }
    }
}