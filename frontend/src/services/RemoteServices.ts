import axios from 'axios';
import Store from '@/store';
import Container from '@/models/Container';
import AuthUser from '@/models/AuthUser';
import Interface from '@/models/Interface';
import router from '@/router';
import Vrf from '@/models/Vrf';
import Lldp from '@/models/Lldp';
import AgentState from '@/models/AgentState';
import Switch from '@/models/Switch';
import AgentConfig from '@/models/AgentConfig';

const httpClient = axios.create();
httpClient.defaults.timeout = 100000;
httpClient.defaults.baseURL = 
    process.env.VUE_APP_ROOT_API || 'http://127.0.0.1:8000';
httpClient.defaults.headers.post['Content-Type'] = 'application/json';
httpClient.interceptors.request.use(
    (config) => {
        if (config.headers !== undefined && !config.headers.Authorization) {
            const token = Store.getters.getToken;

            if (token) {
                config.headers.Authorization = `Token ${token}`;
            }
            else {
                config.headers.Authorization = "";
            }
        }
        return config;
    },
    (error) => Promise.reject(error)
);
httpClient.interceptors.response.use(
    (response) => {
        if (response.data.notification) {
            if (response.data.notification.errorMessages.length) {
                Store.dispatch(
                    'notification',
                    response.data.notification.errorMessages
                );
            }
            response.data = response.data.response;
        }
        return response;
    },
    (error) => Promise.reject(error)
);

export default class RemoteServices {

    static async login(
        username: string,
        password: string
    ) {
        const formData = {
            username,
            password
        };
        return httpClient
            .post(`/api/v1/token/login`, formData)
            .then((response) => {
                const token = response.data.auth_token;
                return token;
            })
            .catch(async (error) => {
                throw Error(await this.errorMessage(error));
            });
    }

    static async getUser(): Promise<AuthUser> {
        return httpClient
            .get('api/v1/accounts/user')
            .then((response) => {
                return new AuthUser(response.data);
            })
            .catch(async (error) => {
                throw Error(await this.errorMessage(error));
            });
    }

    static async getSwitches(): Promise<Switch[]> {
        return httpClient
            .get(`api/v1/switches`)
            .then((response) => {
                return response.data.map((nokia_switch: any) => {
                    return new Switch(nokia_switch);
                });
            })
            .catch(async (error) => {
                throw Error(await this.errorMessage(error));
            })
    }

    static async updateSwitch(
        switch_hostname: string,
        edited_switch: Switch
    ) {
        return httpClient
            .put(`api/v1/switches/update/${switch_hostname}`, edited_switch)
            .then((response) => {
                return response.data;
            })
            .catch(async (error) =>{
                throw Error(await this.errorMessage(error));
            })
    }

    static async createSwitch(
        sr_switch: Switch
    ) {
        return httpClient
            .post('api/v1/switches/create', sr_switch)
            .then((response) => {
                return response.data;
            })
            .catch(async (error) => {
                throw Error(await this.errorMessage(error));
            })
    }

    static async deleteSwitch(
        switch_hostname: string
    ) {
        return httpClient
            .delete(`api/v1/switches/delete/${switch_hostname}`)
            .then((response) => {
                return response.data;
            })
            .catch(async (error) => {
                throw Error(await this.errorMessage(error));
            })
    }

    static async getContainers(): Promise<Container[]> {
        return httpClient
            .get(`api/v1/containers`)
            .then((response) => {
                return response.data.map((container: any) => {
                    return new Container(container);
                });

            })
            .catch(async (error) => {
                throw Error(await this.errorMessage(error));
            });
    }

    static async getInterfaces(
        container: string
    ): Promise <Interface[]> {
        return httpClient
            .get(`api/v1/interfaces/${container}`)
            .then((response) => {
                return response.data.map((iface: any) => {
                    return new Interface(iface);
                });
            })
            .catch(async (error) => {
                throw Error(await this.errorMessage(error));
            });
    }

    static async getInterfaceConfig(
        container: string,
        iface_name: string
        ) {
        return httpClient
            .get(`api/v1/interfaces/config/${container}/${iface_name}`)
            .then((response) => {
                return response.data
            })
            .catch(async (error) => {
                throw Error(await this.errorMessage(error));
            })
    }

    static async getVrfs(
        container: string,
        vrf_type: string
    ): Promise <Vrf[]> {
        return httpClient
            .get(`api/v1/vrfs/${container}/${vrf_type}`)
            .then((response) => {
                return response.data.map((netinst: any) => {
                    return new Vrf(netinst);
                });
            })
            .catch(async (error) => {
                throw Error( await this.errorMessage(error));
            });
    }

    static async getVrfConfig(
        container: string,
        vrf_name: string,
    ) {
        return httpClient
            .get(`api/v1/vrfs/config/${container}/${vrf_name}`)
            .then((response) => {
                return response.data;
            })
            .catch(async (error) => {
                throw Error(await this.errorMessage(error));
            })
            
    }

    static async getLldpNeighbors(
        container: string,
    ): Promise <Lldp[]> {
        return httpClient
            .get(`api/v1/lldp/${container}`)
            .then((response) => {
                return response.data.map((neighbor: any) => {
                    return new Lldp(neighbor);
                });
            })
            .catch( async (error) => {
                throw Error(await this.errorMessage(error));
            });
    }

    static async getAgentConfig(
        hostname: string,
    ) {
        return httpClient
            .get(`api/v1/agentconfig/${hostname}`)
            .then((response) => {
                return response.data.map((agentConfig: any) => {
                    return new AgentConfig(agentConfig);
                });
            })
            .catch(async (error) => {
                throw Error(await this.errorMessage(error));
            })
    }

    static async getAgentState(
        container: string
    ) {
        return httpClient
            .get(`api/v1/agentstate/${container}`)
            .then((response) => {
                return response.data.map((agentState: any) => {
                    return new AgentState(agentState);
                });
            })
            .catch(async (error) => {
                throw Error(await this.errorMessage(error));
            });
    }

    static async setAgentRunning(
        container: string,
        data: unknown
    ) {
        return httpClient
            .post(`api/v1/agentstate/${container}/run`, data)
            .then((response) => {
                return response.data;
            })
            .catch(async (error) => {
                throw Error(await this.errorMessage(error));
            });
    }

    static async errorMessage(error: any): Promise<string> {
        if (error.message === 'Network Error') {
            return 'Unable to connect to server';
        } else if (error.message === 'Request failed with status code 403') {
            await Store.dispatch('logout');
            await router.push({ path: '/' });
            return 'Unauthorized access or expired token';
        } else if (error.message.split(' ')[0] === 'timeout') {
            return 'Request timeout - Server took too long to response';
        } else if (error.response) {
            return error.response.data.message;
        } else {
            console.log(error);
            return 'Unknown error - Contact admin';
        }
    }
}
