<template>
    <v-card>
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
            fixed-header
            :headers="headers"
            :items="switches"
            :search="search"
            :sort-by="['name']"
            @click:row="item => forwarding(item)"
        >
            <template v-slot:top>
                <v-toolbar flat>
                    <v-toolbar-title>Switches</v-toolbar-title>
                    <v-divider
                        class="mx-4"
                        inset
                        vertical
                    ></v-divider>
                    <v-spacer></v-spacer>
                    <v-dialog v-model="dialog" max-width="500px">
                        <template v-slot:activator="{ on, attrs }">
                            <v-btn
                                color="blue"
                                dark
                                class="mb-2"
                                v-bind="attrs"
                                v-on="on"
                            >New Switch
                            </v-btn>
                        </template>
                        <v-card class="ma-0">
                            <v-card-title>
                                <span class="text-h5">{{ formTitle() }}</span>
                            </v-card-title>

                            <v-card-text>
                                <v-container>
                                    <v-form ref="form" lazy-validation>
                                        <v-row>
                                            <v-text-field
                                                v-model="editedSwitch.name"
                                                :rules="[(v) => !!v || 'Name is required']"
                                                label="Name"
                                                required
                                            />
                                        </v-row>
                                        <v-row>
                                            <v-text-field
                                                v-model="editedSwitch.hostname"
                                                :rules="[(v) => !!v || 'Hostname is required']"
                                                label="Hostname"
                                                required
                                            />
                                        </v-row>
                                        <v-row>
                                            <v-text-field
                                                v-model="editedSwitch.switch_type"
                                                :rules="[(v) => !!v || 'Type is required']"
                                                label="Switch Type"
                                                required
                                            />
                                        </v-row>
                                        <v-row>
                                            <v-text-field
                                                v-model="editedSwitch.ipv4"
                                                :rules="[(v) => !!v || 'IPv4 address is required']"
                                                label="IPv4 Address"
                                                required
                                            />
                                        </v-row>
                                        <v-row>
                                            <v-text-field
                                                v-model="editedSwitch.ipv6"
                                                label="IPv6 Address"
                                            />
                                        </v-row>
                                        <v-row>
                                            <v-text-field
                                                v-model="editedSwitch.port"
                                                :rules="[(v) => !!v || 'Port is required']"
                                                label="Port"
                                                required
                                            />
                                        </v-row>
                                    </v-form>
                                </v-container>
                            </v-card-text>

                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn color="blue darken-1" text @click="close()">Cancel</v-btn>
                                <v-btn color="blue darken-1" text @click="save()">Save</v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                    <v-dialog v-model="dialogDelete" max-width="500px">
                        <v-card class="ma-0">
                            <v-card-title class="text-h6">Are you sure you want to delete this Switch?</v-card-title>
                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn color="blue darken-1" text @click="closeDelete()">Cancel</v-btn>
                                <v-btn color="blue darken-1" text @click="deleteConfirm()">OK</v-btn>
                                <v-spacer></v-spacer>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                </v-toolbar>
            </template>
            <template v-slot:[`item.actions`]="{ item }">
                <v-icon
                    small
                    class="mr-2"
                    @click.stop.prevent="editSwitch(item)"
                >mdi-pencil
                </v-icon>
                <v-icon
                    small
                    @click.stop.prevent="deleteSwitch(item)"
                >mdi-delete
                </v-icon>
            </template>
        </v-data-table>
    </v-card>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import RemoteServices from '@/services/RemoteServices';
import Switch from '@/models/Switch';

@Component
export default class SwitchesView extends Vue {

    search = '';
    switches: Switch[] = [];
    editedIndex = -1;
    dialog = false;
    dialogDelete = false;
    editedSwitch: Switch = new Switch();

    headers = [
        { text: 'Name', value: 'name' },
        { text: 'Hostname', value: 'hostname' },
        { text: 'Type', value: 'switch_type' },
        { text: 'Ipv4 Address', value: 'ipv4' },
        { text: 'IPv6 Address', value: 'ipv6' },
        { text: 'Port', value: 'port' },
        { text: 'Actions', value: 'actions', sortable: false }
    ];

    async created() {
        try {
            this.switches = await RemoteServices.getSwitches();
        }
        catch (error) {
            await this.$store.dispatch('error', error);
        }
    }

    async forwarding(sr_switch: Switch) {
        try {
            this.$store.dispatch('currentSwitch', sr_switch);
            await this.$router.push({ name: 'switch-options', params: { hostname: sr_switch.hostname } });
        } catch (error) {
            await this.$store.dispatch('error', error);
        }
    }

    formTitle() {
        return this.editedIndex === -1 ? 'New Switch' : 'Edit Switch';
    }

    editSwitch(sr_switch: Switch) {
        this.editedIndex = this.switches.indexOf(sr_switch);
        this.editedSwitch = sr_switch;
        this.dialog = true;
    }

    deleteSwitch(sr_switch: Switch) {
        this.editedIndex = this.switches.indexOf(sr_switch);
        this.editedSwitch = sr_switch;
        this.dialogDelete = true;
    }

    async deleteConfirm() {
        await RemoteServices.deleteSwitch(this.editedSwitch.hostname);
        this.switches = await RemoteServices.getSwitches();
        this.closeDelete()
    }

    close() {
        this.dialog = false;
        this.$nextTick(() => {
            this.editedSwitch = new Switch;
            this.editedIndex = -1;
        })
    }

    closeDelete() {
        this.dialogDelete = false;
        this.$nextTick(() => {
            this.editedSwitch = new Switch();
            this.editedIndex = -1;
        })
    }

    async save() {
        if (this.editedIndex > -1) {
            await RemoteServices.updateSwitch(this.editedSwitch.hostname, this.editedSwitch);
            this.switches = await RemoteServices.getSwitches();
        } else {
            await RemoteServices.createSwitch(this.editedSwitch);
            this.switches = await RemoteServices.getSwitches();
        }
        this.close()
    }


}
</script>

<style lang="scss" scoped>
.v-card {
    margin: 80px;
}

::v-deep tr:hover {
    cursor: pointer;
}
</style>