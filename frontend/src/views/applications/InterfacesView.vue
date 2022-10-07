<template>
    <v-card>
        <v-card-title class="text-center justify-center py-6">
        Interfaces of {{ this.switch.name }}
        </v-card-title>
        <v-spacer></v-spacer>
        <v-card-title>
            <v-text-field
                v-model="search"
                append-icon="mdi-magnify"
                label="Search"
                single-line
                hide-details
            ></v-text-field>
        </v-card-title>
        <v-data-table
            class="row-pointer"
            fixed-header
            :headers="headers"
            :items="ifaces"
            :search="search"
        >
            <template v-slot:[`item.oper_state`]="{ item }">
                <v-chip :color="getColor(item.oper_state)" dark>{{ item.oper_state }}</v-chip>
            </template>
            <template v-slot:[`item.config`]="{ item }">
                <v-btn 
                    class="ma-2"
                    icon
                    text
                    color="#27439c"
                    @click="showConfig(item)"
                >
                    <v-icon>mdi-file-document-outline</v-icon>
                </v-btn>
            </template>
        </v-data-table>
        <v-dialog
            v-model="configDialog"
            max-width="75%"
            @input="configDialog = false"
            @keydown.esc="configDialog = false"
        >
            <v-card
                class="ma-0"
                >
                <v-card-title>Configuration</v-card-title>
                <v-card-text class="text-left">
                    <pre>{{ this.config }}</pre>
                </v-card-text>
                <v-card-actions>
                    <v-spacer />
                    <v-btn 
                        dark
                        color="#27439c"
                        @click="configDialog =! configDialog"
                    >Close</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-card>    
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import RemoteServices from '@/services/RemoteServices';
import Interface from '@/models/Interface';
import Switch from '@/models/Switch';

@Component
export default class InterfacesView extends Vue {
    switch: Switch | null = this.$store.getters.getCurrentSwitch;
    ifaces: Interface[] = [];
    configDialog = false;
    filterDialog = false;
    filters = {
        'admin_state': [] as string[],
        'oper_state': [] as string[],
        'oper_down_reason': [] as string[],
    };
    
    activeFilters = {} as any;
    config = '';
    search = '';
    headers = [
        {
            text: 'Name',
            value: 'name',
            align: 'start'
        },
        {
            text: 'Admin-state',
            value: 'admin_state',
        },
        {
            text: 'Oper-state',
            value: 'oper_state'
        },
        {
            text: 'Oper-down-reason',
            value: 'oper_down_reason'
        },
        {
            text: 'Config',
            value: 'config'
        }
    ];

    async created() {
        try {
            if (!this.switch?.hostname) {
                await this.$router.push({ name: 'switches' });
            }
            
            this.ifaces = await RemoteServices.getInterfaces(this.$store.getters.getCurrentSwitch.hostname);
            console.log(this.ifaces)
            this.initFilters()
        } catch (error) {
            await this.$store.dispatch('error', error);
        }
    }

    async showConfig(iface: Interface) {
        try {
            this.config = await RemoteServices.getInterfaceConfig(this.$store.getters.getCurrentSwitch.hostname, iface.name);
            this.config = JSON.stringify(this.config, null, 2);
            this.configDialog = !this.configDialog;
        }
        catch (error) {
            await this.$store.dispatch('error', error);
        }
    }

    initFilters() {
        try {
            Object.keys(this.filters).forEach(key => {
            this.filters[key as keyof typeof this.filters] = this.ifaces.map((iface) => {
                return iface[key as keyof typeof iface];
            })
            .filter((value, index, self) => {
                return self.indexOf(value) === index
            });
            })
            this.activeFilters = Object.assign({}, this.filters);
        }
        catch (error) {
            this.$store.dispatch('error', error);
        }
        
    }

    getColor(oper_state: string) {
        if (oper_state === 'down') {
            return 'red';
        } else {
            return 'green';
        }
    }

    
    
}
</script>

<style lang="scss" scoped>
.v-card {
    margin: 80px;
}
</style>