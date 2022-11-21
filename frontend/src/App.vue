<template>
  <v-app id="app">
    <top-bar />
    <div class="scrollbar">
      <error-message />
      <notification />
      <router-view />
    </div>
  </v-app>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import TopBar from '@/components/TopBar.vue';
import ErrorMessage from '@/components/ErrorMessage.vue';
import Notification from '@/components/Notification.vue';
import axios from 'axios';
import '@/assets/css/_global.scss';
import '@/assets/css/_scrollbar.scss';

@Component({
  components: { TopBar, ErrorMessage, Notification }
})

export default class App extends Vue {

  created() {
    axios.interceptors.response.use(undefined, (err) => {
      return new Promise(() => {
        if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
          this.$store.dispatch('logout');
        }
        throw err;
      });
    });
  }
  
}
</script>

<style scoped>
#app {
  background-image: url('./assets/nokia-background.png');
  background-position: 0 0;
  background-repeat: no-repeat;
  background-size: cover;
  height: 100%;
  min-height: 100vh;
  width: 100%;
  color: #2c3e50;
  content: ' ';
  display: flex;
  flex-direction: column;
  left: 0;
  margin: 0 !important;
  overflow: hidden;
  position: absolute;
  text-align: center;
  top: 0;
  z-index: 1;
}

.application--wrap {
  min-height: initial !important;
}
</style>
