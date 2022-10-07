<template>
  <v-card class="ma-0">
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
      :headers="headers_config"
      :search="search"
      :items="targets_config"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Software Agent Config</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="newTestDialog" max-width="500px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="blue" dark class="mb-2" v-bind="attrs" v-on="on"
                >New Test
              </v-btn>
            </template>
            <v-card class="ma-0">
              <v-card-title>
                <span class="text-h5">New Test</span>
              </v-card-title>

              <v-card-text>
                <software-agent @dialogClose="closeDialog"></software-agent>
              </v-card-text>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
    </v-data-table>
    <v-divider class="mx-4" inset horizontal></v-divider>
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
      :headers="headers_state"
      :items="targets_state"
      :search="search"
    >
        <template v-slot:top>
            <v-toolbar flat>
                <v-toolbar-title>Software Agent State</v-toolbar-title>
                <v-divider class="mx-4" inset vertical></v-divider>
                <v-spacer></v-spacer>
            </v-toolbar>
        </template>
    </v-data-table>
  </v-card>
</template>

<script lang="ts">
import AgentState from "@/models/AgentState";
import AgentConfig from "@/models/AgentConfig";
import Container from "@/models/Container";
import Switch from "@/models/Switch";
import RemoteServices from "@/services/RemoteServices";
import { Component, Vue } from "vue-property-decorator";
import SoftwareAgent from "./SoftwareAgent.vue";

@Component({
  components: { SoftwareAgent },
})
export default class SoftwareAgentState extends Vue {
  search = "";
  targets_state: AgentState[] = [];
  targets_config: AgentConfig[] = [];
  container: Container | null = this.$store.getters.getCurrentContainer;
  switch: Switch | null = this.$store.getters.getCurrentSwitch;

  newTestDialog = false;

  headers_config = [
      { text: "IP-FQDN", value: "IP-FQDN" },
      { text: "Admin-state", value: "admin-state" },
      { text: "Network Instance", value: "network-instance" },
      { text: "Test Tool", value: "test-tool" },
      { text: "Source-IP", value: "source-ip" },
      { text: "Destination Port", value: "port" },
      { text: "Number of Tests", value: "number-of-tests" },
      { text: "Number of Packets", value: "number-of-packets" },
      { text: "Interval Period", value: "interval-period" }
  ];

  headers_state = [
    { text: "IP-FQDN / Network Instance", value: "ip_fqdn" },
    { text: "Admin-state", value: "admin_state" },
    { text: "Last Update", value: "last_update" },
    { text: "Tests Performed", value: "tests_performed" },
    { text: "Successful tests", value: "success_tests" },
    { text: "Unsuccessful tests", value: "unsuccess_tests" },
    { text: "Status", value: "status_up" },
    { text: "RTT Min (ms)", value: "rtt_min" },
    { text: "RTT Max (ms)", value: "rtt_max" },
    { text: "RTT Average (ms)", value: "rtt_avg" },
    { text: "RTT Std Dev (ms)", value: "rtt_std" },
  ];

  async created() {
    try {
      if (!this.switch?.hostname) {
        await this.$router.push({ name: "switches" });
      }

      this.targets_state = await RemoteServices.getAgentState(
        this.$store.getters.getCurrentSwitch.hostname
      );
      this.targets_config = await RemoteServices.getAgentConfig(
        this.$store.getters.getCurrentSwitch.hostname
      );
    } catch (error) {
      await this.$store.dispatch("error", error);
    }
  }

  closeDialog(bool: boolean) {
    this.newTestDialog = bool;
  }
}
</script>