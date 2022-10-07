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
            class="row-pointer"
            @click:row="item => forwarding(item)"
            fixed-header
            :headers="headers"
            :items="containers"
            :search="search"
        ></v-data-table>
    </v-card>
            

</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import RemoteServices from '../services/RemoteServices';
import Container from '../models/Container';

@Component
export default class DashboardView extends Vue {

    containers: Container[] = [];
    search = '';
    headers = [
        {
            text: 'Name',
            value: 'name',
            align: 'start',
        },
        {
            text: 'ID', value: 'container_id',
        },
        
        {
            text: 'IPv4 Address', value: 'ip_address',
        },
        {
            text: 'IPv6 Address', value: 'ip6_address',
        },
        {
            text: 'Image', value: 'image',
        },
        {
            text: 'State', value: 'state',
        }
    ];

    async created() {

        try {
            this.containers = await RemoteServices.getContainers();
        } catch (error) {
            console.log(error);
            await this.$store.dispatch('error', error);
        }
    }

    async forwarding(container: Container) {
        try {
            await this.$store.dispatch('currentContainer', container);
            await this.$router.push({ name: 'container-options' });
        } catch (error) {
            await this.$store.dispatch('error', error);
        }
    }

}
</script>

<style lang="scss" scoped>

.row-pointer > .v-data-table__wrapper > table > tbody > tr > td:hover {
    cursor: pointer;
}

.v-card {
    margin: 80px;
}
</style>