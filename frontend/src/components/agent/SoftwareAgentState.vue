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
          <v-spacer></v-spacer>
          <v-switch
            v-model="switch_btn"
            class="mb-2"
            :label="`Software Agent is ${parseSwitchValue().toString()}`"
            @change="onChangeSwitch()"
          ></v-switch>
        </v-toolbar>
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
      <template v-slot:[`item.change_state`]="{ item }">
        <v-btn
          class="ma-2"
          :color="adminStateColor(item['admin-state'])"
          @click="onChangeAdminState(item['IP-FQDN'], item['admin-state'])"
          >{{ getBtnTextAdminState(item["admin-state"]) }}</v-btn
        >
      </template>
      <template v-slot:[`item.delete_test`]="{ item }">
        <v-btn color="red" class="ma-2" @click="deleteTest(item['IP-FQDN'])"
          >Delete</v-btn
        >
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
      <template v-slot:[`item.status_up`]="{ item }">
        <v-chip :color="getColor(item.status_up)" dark class="black--text">{{
          item.status_up
        }}</v-chip>
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
  teste = 1;
  interval: number | undefined;
  switch_btn = false;
  switch_admin_state: boolean | undefined;

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
    { text: "Interval Period", value: "interval-period" },
    { text: "Enable/Disable", value: "change_state", align: "center" },
    { text: "Delete Test", value: "delete_test", align: "center" },
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
      if (
        (await RemoteServices.getAgentAdminState(
          this.$store.getters.getCurrentSwitch.hostname
        )) === "enable"
      ) {
        this.switch_btn = true;
      } else {
        this.switch_btn = false;
      }
      this.targets_state = await RemoteServices.getAgentState(
        this.$store.getters.getCurrentSwitch.hostname
      );
      this.targets_config = await RemoteServices.getAgentConfig(
        this.$store.getters.getCurrentSwitch.hostname
      );
      this.interval = setInterval(async () => {
        this.targets_state = await RemoteServices.getAgentState(
          this.$store.getters.getCurrentSwitch.hostname
        );
      }, 5000);
    } catch (error) {
      await this.$store.dispatch("error", error);
    }
  }

  parseSwitchValue() {
    if (this.switch_btn) {
      return "running";
    } else {
      return "stopped";
    }
  }

  switch_btn_admin_state(admin_state: string) {
    if (admin_state === "enable") {
      return true;
    } else {
      return false;
    }
  }

  async onChangeAdminState(destinationIP: string, admin_state: string) {
    console.log(destinationIP + " " + admin_state);
    let admin_state_change = "";
    if (admin_state === "enable") {
      admin_state_change = "disable";
    } else {
      admin_state_change = "enable";
    }
    const formData = {
      destinationIP: destinationIP,
      admin_state: admin_state_change,
    };
    await RemoteServices.setAgentTestAdminState(
      this.$store.getters.getCurrentSwitch.hostname,
      formData
    );
    this.targets_config = await RemoteServices.getAgentConfig(
      this.$store.getters.getCurrentSwitch.hostname
    );
  }

  async onChangeSwitch() {
    if (this.switch_btn) {
      const formData = {
        admin_state: "enable",
      };
      await RemoteServices.setAgentAdminState(
        this.$store.getters.getCurrentSwitch.hostname,
        formData
      );
    } else {
      const formData = {
        admin_state: "disable",
      };
      await RemoteServices.setAgentAdminState(
        this.$store.getters.getCurrentSwitch.hostname,
        formData
      );
    }
  }

  async deleteTest(ip_fqdn: string) {
    console.log(ip_fqdn);
    const formData = {
      destinationIP: ip_fqdn,
    };
    await RemoteServices.deleteAgentTest(
      this.$store.getters.getCurrentSwitch.hostname,
      formData
    );
    this.targets_config = await RemoteServices.getAgentConfig(
      this.$store.getters.getCurrentSwitch.hostname
    );
  }

  getBtnTextAdminState(admin_state: string) {
    if (admin_state === "enable") {
      return "STOP";
    } else {
      return "RUN";
    }
  }

  adminStateColor(admin_state: string) {
    console.log("OPAAAA " + admin_state);
    if (admin_state === "enable") {
      return "red";
    } else {
      return "green";
    }
  }

  getColor(status_up: string) {
    if (status_up === 'Service up') {
      return 'green';
    }
    else if (status_up === 'Service down') {
      return 'red';
    } else {
      return 'yellow';
    }
  }

  async closeDialog(bool: boolean) {
    this.targets_config = await RemoteServices.getAgentConfig(
      this.$store.getters.getCurrentSwitch.hostname
    );
    this.newTestDialog = bool;
  }

  async beforeDestroy() {
    clearInterval(this.interval);
  }
}
</script>