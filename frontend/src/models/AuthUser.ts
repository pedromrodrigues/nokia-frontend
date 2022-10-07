import { ISOtoString } from "@/services/ConvertDate";

export default class AuthUser {
    username!: string;
    is_staff!: boolean;
    name: string | null = null;
    email: string | null = null;
    last_login!: string;
    date_joined!: string;

    constructor(jsonObj?: AuthUser) {
        if (jsonObj) {
            this.username = jsonObj.username;
            this.is_staff = jsonObj.is_staff;
            this.name = jsonObj.name;
            this.email = jsonObj.email;
            this.last_login = jsonObj.last_login;
            this.date_joined = jsonObj.date_joined;

            if (jsonObj.last_login) {
                this.last_login = ISOtoString(this.last_login);
            }
            if (jsonObj.date_joined) {
                this.date_joined = ISOtoString(this.date_joined);
            }
        }
    }
}