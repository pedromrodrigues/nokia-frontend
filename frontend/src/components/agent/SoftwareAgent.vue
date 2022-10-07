<template>
    <div class="text-center">
        <v-container fluid>
            <v-form
                ref="form"
                v-model="valid"
                lazy-validation
            >

                <v-select
                    v-model="netinst"
                    :items="ipVrfs"
                    item-text="name"
                    label="Select IP-VRF"
                    :rules="ipVrfRules"
                    outlined
                    solo
                    required
                ></v-select>
                <v-select
                    v-model="testTool"
                    :items="testTools"
                    label="Choose a testing tool"
                    :rules="testToolRules"
                    outlined
                    solo
                    required
                    v-on:change="isDisabled()"
                ></v-select>
                <v-text-field
                    v-model="destinationIP"
                    label="Destination IP"
                    :rules="destinationIPRules"
                    outlined
                    required
                ></v-text-field>
                <v-text-field
                    v-model="port"
                    label="Port"
                    outlined
                    :disabled=disabled
                ></v-text-field>
                <v-text-field
                    v-model="sourceIP"
                    label="Source IP"
                    :rules="sourceIPRules"
                    outlined
                    required
                ></v-text-field>
                <v-text-field
                    v-model="numberTests"
                    label="Number of total tests"
                    :rules="numberTestsRules"
                    outlined
                    required
                    type="number"
                ></v-text-field>
                <v-text-field
                    v-model="numberPackets"
                    label="Number of packets for each test"
                    outlined
                    required
                    type="number"
                ></v-text-field>
                <v-select
                    v-model="time"
                    :items="timeInterval"
                    label="Time between each test in seconds"
                    outlined
                    clearable
                ></v-select>

                <v-btn
                    color="grey"
                    class="mr-4"
                    @click="reset"
                >
                Reset
                </v-btn>
                <v-btn
                    color="blue"
                    class="mr-4"
                    @click="close"
                >Cancel
                </v-btn>
                <v-btn
                    :disabled="!valid"
                    color="blue"
                    class="mr-4"
                    @click="runTest"
                >
                Run
                </v-btn>

            </v-form>
        </v-container>
    </div>
    
</template>

<script lang="ts">
import { Component, Vue} from 'vue-property-decorator';
import Vrf from '@/models/Vrf';
import RemoteServices from '@/services/RemoteServices';
import SoftwareAgentState from '@/components/agent/SoftwareAgentState.vue';
import Switch from '@/models/Switch';


@Component({
    components: { 'software-agent-state': SoftwareAgentState },
})

export default class SoftwareAgent extends Vue {
    valid = true;
    disabled = true;
    switch: Switch | null = this.$store.getters.getCurrentSwitch;
    ipVrfs: Vrf[] = [];
    destinationIP = '';
    netinst = '';
    sourceIP = '';
    numberPackets = '';
    numberTests = '';
    port = '';
    testTool = '';
    time = '';
    testTools = [ 'ping', 'httping' ];
    timeInterval = [ '1', '5', '10', '15', '30', '60', '120', '9999999'];
    

    ipVrfRules = [ (v:any) => !!v || 'IP-VRF is required' ];
    testToolRules = [ (v:any) => !!v || 'Test tool is required' ];
    destinationIPRules = [ (v: any) => !!v || 'Destination IP is required' ];
    sourceIPRules = [ (v:any) => !!v || 'Source IP is required'];
    numberTestsRules = [ (v:any) => !!v || 'Number of tests is required.' ];

    async created() {
        try {
            if (!this.switch?.hostname) {
                await this.$router.push({ name: 'switches' });
            }
            this.ipVrfs = await RemoteServices.getVrfs(this.$store.getters.getCurrentSwitch.hostname, 'ip-vrf');
        } catch (error) {
            await this.$store.dispatch('error', error);
        }
    }

    async runTest() {
        let t = (this.$refs.form as HTMLFormElement).validate();
        const formData = {
            'destinationIP': this.destinationIP,
            'netinst': this.netinst,
            'sourceIP': this.sourceIP,
            'numberTests': this.numberTests,
            'testTool': this.testTool,
            'numberPackets': this.numberPackets,
            'port': this.port,
            'time': this.time
        };
        try {
            await RemoteServices.setAgentRunning(this.$store.getters.getCurrentSwitch.hostname, formData);
            this.close();
        } catch (error) {
            await this.$store.dispatch('error', error);
        }
    }

    reset() {
        this.destinationIP = '';
        this.sourceIP = '';
        this.numberPackets = '';
        this.numberTests = '';
        this.port = '';
        this.testTool = '';
        this.time = '';
        (this.$refs.form as HTMLFormElement).reset();
    }

    isDisabled() {
        if (this.testTool === 'httping') {
            this.disabled = false;
        }
        else if (this.testTool === 'ping') {
            this.disabled = true;
        }
    }

    close() {
        this.$emit('dialogClose', false);
    }


}
</script>