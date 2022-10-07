export default class Container {
    container_id!: string;
    name!: string;
    ip_address!: string;
    ip6_address!: string;
    image!: string;
    state!: string;

    constructor(jsonObj?: Container) {
        if (jsonObj) {
            this.container_id = jsonObj.container_id;
            this.name = jsonObj.name;
            this.ip_address = jsonObj.ip_address;
            this.ip6_address = jsonObj.ip6_address;
            this.image = jsonObj.image;
            this.state = jsonObj.state;
        }
    }
}