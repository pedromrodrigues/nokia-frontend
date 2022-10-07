import { ISOtoString } from "@/services/ConvertDate";

export default class Lldp {
    iface_name!: string;
    neighbor_id!: string;
    neighbor_first_message!: string;
    neighbor_last_update!: string;
    neighbor_name!: string;
    neighbor_iface!: string;

    constructor(jsonObj?: Lldp) {
        if (jsonObj) {
            this.iface_name = jsonObj.iface_name;
            this.neighbor_id = jsonObj.neighbor_id;
            this.neighbor_first_message = jsonObj.neighbor_first_message;
            this.neighbor_last_update = jsonObj.neighbor_last_update;
            this.neighbor_name = jsonObj.neighbor_name;
            this.neighbor_iface = jsonObj.neighbor_iface;

            if (jsonObj.neighbor_first_message) {
                this.neighbor_first_message = ISOtoString(this.neighbor_first_message);
            }
            if (jsonObj.neighbor_last_update) {
                this.neighbor_last_update = ISOtoString(this.neighbor_last_update);
            }
        }

    }


}