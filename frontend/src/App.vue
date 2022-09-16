<template>
  <v-app id="app">
    <top-bar />
    <div class="scrollbar">
      <router-view />
    </div>
  </v-app>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import TopBar from './components/TopBar.vue';
import axios from 'axios';
import './assets/css/_global.scss';
import './assets/css/_scrollbar.scss';

@Options({
  options: { TopBar }
})

export default class App extends Vue {

  beforeCreate() {
    this.$store.commit('initializeStore');

    const token = this.$store.state.token;

    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token;
    } else {
      axios.defaults.headers.common['Authorization'] = "";
    }

  }

  created() {
    console.log('lol')
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
