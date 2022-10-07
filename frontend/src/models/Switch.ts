//import { ISOtoString } from "@/services/ConvertDate";

export default class Switch {
    hostname!: string;
    name!: string;  
    switch_type!: string;
    ipv4!: string;
    port!: number;
    ipv6: string | null = null;

    constructor(jsonObj?: Switch) {
        if (jsonObj) {
            this.hostname = jsonObj.hostname;
            this.name = jsonObj.name;
            this.switch_type = jsonObj.switch_type;
            this.ipv4 = jsonObj.ipv4;
            this.ipv6 = jsonObj.ipv6;
            this.port = jsonObj.port;
        }
    }
}