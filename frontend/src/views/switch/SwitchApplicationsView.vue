<template>
    <v-card>
        <v-card-title class="text-center justify-center py-6">
        {{ title }}
        </v-card-title>

        <v-spacer></v-spacer>

        <v-tabs
            v-model="tab"
            grow
        >
            <v-tab
                v-for="item in items"
                :key="item"
            >
                {{ item }}
            </v-tab>
        </v-tabs>

        <v-tabs-items v-model="tab">
            <v-tab-item
                v-if="item = 'Configurations'"
            >
                <switch-configurations />
            </v-tab-item>
            <v-tab-item
                v-if="item = 'Software Agent'"
            >
                <software-agent-state />
            </v-tab-item>
        </v-tabs-items>
            

    </v-card>
    
</template>

<script lang="ts">
/* eslint-disable */

import Switch from '@/models/Switch';
import { Component, Vue } from 'vue-property-decorator';
import SwitchConfigurations from '@/components/applications/SwitchConfigurations.vue';
//import SoftwareAgent from '@/components/agent/SoftwareAgent.vue';
import SoftwareAgentState from '@/components/agent/SoftwareAgentState.vue'

@Component({
    components: { SwitchConfigurations, 'software-agent-state': SoftwareAgentState },
})
export default class SwitchApplicationsView extends Vue {
    
    switch: Switch | null = this.$store.getters.getCurrentSwitch;
    title = "Switch " + this.switch?.name + " Options";
    tab = null;
    items = [
        'Configurations',
        'Software Agent',
    ]

    async created() {
        if (!this.switch?.hostname) {
            await this.$router.push({ name: 'switches' });
        }
    }
    
}
</script>

<style lang="scss" scoped>

.v-card {
    margin: 80px;
}
</style>