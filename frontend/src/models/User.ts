export default class User {
    name!: string;
    email!: string;
    org_number: number | null = null;
    contact!: string;
    created_at!: string;
    admin!: boolean;

    constructor(jsonObj?: User) {
        if (jsonObj) {
            this.name = jsonObj.name;
            this.email = jsonObj.email;
            this.org_number = jsonObj.org_number;
            this.admin = jsonObj.admin;
        }
    }
}