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
            :items="lldp_neighbors"
            :search="search"
        ></v-data-table>
    </v-card>    
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import RemoteServices from '@/services/RemoteServices';
import Lldp from '@/models/Lldp';
import Switch from '@/models/Switch';

@Component
export default class LldpView extends Vue {

    switch: Switch | null = this.$store.getters.getCurrentSwitch;
    lldp_neighbors: Lldp[] = [];

    search = '';
    headers = [
        {
            text: 'Interface Name',
            value: 'iface_name',
            align: 'start'
        },
        {
            text: 'Neighbor',
            value: 'neighbor_id'
        },
        {
            text: 'Neighbor System Name',
            value: 'neighbor_name'
        },
        {
            text: 'Neighbor First Message',
            value: 'neighbor_first_message'
        },
        {
            text: 'Neighbor Last Update',
            value: 'neighbor_last_update'
        },
        {
            text: 'Neighbor Port',
            value: 'neighbor_iface'
        }
    ];

    async created() {
        try {
            if (!this.switch?.hostname) {
                await this.$router.push({ name: 'switches' });
            }
            this.lldp_neighbors = await RemoteServices.getLldpNeighbors(this.$store.getters.getCurrentSwitch.hostname);
        } catch (error) {
            await this.$store.dispatch('error', error);
        }
    }
    
}
</script>

<style lang="scss" scoped>
.v-card {
    margin: 80px;
}
</style>