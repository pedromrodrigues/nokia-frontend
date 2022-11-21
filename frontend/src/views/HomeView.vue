<template>
  <div class="container">
    <login-card @onSubmit="login"></login-card>
  </div>
</template>

<script lang="ts">
/* eslint-disable */

import { Component , Vue } from 'vue-property-decorator';
import LoginCard from '@/components/LoginCard.vue';
import { AxiosError } from 'axios';

@Component({
  components: { 'login-card': LoginCard }
})

export default class HomeView extends Vue {

  async created() {
    if (this.$store.getters.isAuthenticated) {
      await this.$router.push({ name: 'switches' });
    }
  }

  async login(username: string, password: string) {
    const formData = {
      username,
      password
    }
    try {
      await this.$store.dispatch('login', formData);
      await this.$router.push({ name: 'switches' });
    
    } catch (error) {
      await this.$store.dispatch('error', error);
    }
  }
}

</script>

<style lang="scss" scoped>
.container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  align-content: center;
  height: 100%;

  .v-btn {
    margin: 5px;
    text-decoration: white;
  }
}
</style>

