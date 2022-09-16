export default class Container {
    container_id!: string;
    name!: string;
    IPAddress!: string;
    IP6Address!: string;
    image!: string;
    state!: string;

    constructor(jsonObj?: Container) {
        if (jsonObj) {
            this.container_id = jsonObj.container_id;
            this.name = jsonObj.name;
            this.IPAddress = jsonObj.IPAddress;
            this.IP6Address = jsonObj.IP6Address;
            this.image = jsonObj.image;
            this.state = jsonObj.state;
        }
    }
}