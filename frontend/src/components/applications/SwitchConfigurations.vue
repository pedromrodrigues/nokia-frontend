<template>
    <div class="text-center">
        <v-container fluid>
            <v-row align="center">
                <v-col
                    v-for="option in configuration_options"
                    :key="option"
                    cols="12"
                    sm="6"
                >
                    <v-btn
                        class="ma-2"
                        color="primary"
                        @click="check(option)"
                    >
                    {{ option }}
                    </v-btn>
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Interface from '@/models/Interface';


@Component
export default class SwitchConfigurations extends Vue {

    configuration_options = [
        'Interfaces',
        'LLDP Neighbors',
        'IP-VRFs',
        'MAC-VRFs',
    ];

    ifaces: Interface[] = [];

    async check(option: string) {
        if (option === 'Interfaces') {
            await this.$router.push({ name: 'interfaces', params: { hostname: this.$store.getters.getCurrentSwitch.hostname } })
        }
        if (option === 'IP-VRFs') {
            await this.$router.push({
                path: `/switches/${this.$store.getters.getCurrentSwitch.hostname}/vrfs`,
                query: { vrf_type: 'ip-vrf'}
            });
        }
        if (option === 'MAC-VRFs') {
            await this.$router.push({
                path: `/switches/${this.$store.getters.getCurrentSwitch.hostname}/vrfs`,
                query: { vrf_type: 'mac-vrf'}
            });
        }
        if (option === 'LLDP Neighbors') {
            await this.$router.push({ name: 'lldp', params: { hostname: this.$store.getters.getCurrentSwitch.hostname } })
        }
    }
    
}
</script>